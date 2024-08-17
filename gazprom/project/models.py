import datetime
import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import JSONField
from django.utils import timezone
from django.core.exceptions import ValidationError

User = get_user_model()


def employee_validate_birth_date(value):
    min_date = datetime.datetime(1924, 1, 1)
    max_date = timezone.now().date()

    if value < min_date:
        raise ValidationError(f'Birth date cannot be earlier than {min_date.strftime("%Y-%m-%d")}.')
    if value > max_date:
        raise ValidationError(f'Birth date cannot be later than the current date.')


def validate_utc_offset(value):
    try:
        if not (value.startswith('+') or value.startswith('-')):
            raise ValidationError('UTC offset must start with + or -.')

        offset_hours = float(value[1:])

        if not -12 <= offset_hours <= 14:
            raise ValidationError('UTC offset must be between -12 and +14 hours.')

        if not (len(value) == 5 and value[3] == ':'):
            raise ValidationError('UTC offset format is invalid. It should be in the format of +HH:MM or -HH:MM.')
    except ValueError:
        raise ValidationError('UTC offset is not a valid number.')


class TimeZones(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Уникальный идентификатор статуса (PK)"
    )
    name = models.CharField(
        unique=True,
        max_length=64,
        verbose_name='Название часового пояса',
        validators=[
            MinLengthValidator(1),
            RegexValidator(
                regex=r'^[a-zA-Z/]+$',
                message='Название должно содержать только латинские буквы и /'
            )
        ]
    )
    abbrev = models.CharField(
        max_length=5,
        verbose_name='Аббревиатура часового пояса',
        validators=[
            MinLengthValidator(3),
        ]
    )
    utc_offset = models.CharField(validators=[validate_utc_offset], max_length=5,
                                  verbose_name='Смещение относительно UTC'
                                  )

    class Meta:
        db_table = 'time_zones'

    def __str__(self):
        return f'{self.name} ({self.abbrev})'


class Departments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True,
                          verbose_name="Уникальный идентификатор статуса (PK)"
                          )
    parent_department = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name='sub_departments')
    title = models.CharField(max_length=64, verbose_name='Название отдела', unique=True)
    count_employee = models.PositiveIntegerField(
        verbose_name='Количество сотрудников в департаменте/отделе',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000)
        ]
    )
    count_project = models.PositiveIntegerField(
        verbose_name='Количество проектов в департаменте/отделе',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.title


class Vacations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    start_date = models.DateTimeField(verbose_name='Дата начала отпуска')
    end_date = models.DateTimeField(verbose_name='Дата окончания отпуска')

    class Meta:
        db_table = 'vacations'

    def __str__(self):
        return f'Vacation from {self.start_date} to {self.end_date}'


class EmployeeStatuses(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS_ON_VACATION = 'on_vacation'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Активный'),
        (STATUS_INACTIVE, 'Неактивный'),
        (STATUS_ON_VACATION, 'В отпуске'),
    ]

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Уникальный идентификатор статуса (PK)"
    )
    name = models.CharField(
        max_length=64,
        choices=STATUS_CHOICES,
        validators=[MinLengthValidator(1)],
        verbose_name="Статус сотрудника"
    )
    is_selected = models.BooleanField(
        default=False,
        verbose_name="Признак выбранного значения статуса"
    )

    def __str__(self):
        return f"{self.name} (Selected: {'Yes' if self.is_selected else 'No'})"

    class Meta:
        db_table = 'employee_statuses'
        ordering = ('name',)
        verbose_name = 'Статус сотрудника'
        verbose_name_plural = 'Статусы сотрудников'

        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_employee_status_name')
        ]


class EmployeeHireTypes(models.Model):
    HIRE_TYPE_PERMANENT = 'Штатный'
    HIRE_TYPE_OUTSOURCED = 'Аутсорс'

    HIRE_TYPE_CHOICES = [
        (HIRE_TYPE_PERMANENT, 'Штатный'),
        (HIRE_TYPE_OUTSOURCED, 'Аутсорс'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Уникальный идентификатор типа найма (PK)"
    )
    name = models.CharField(
        max_length=64,
        choices=HIRE_TYPE_CHOICES,
        validators=[MinLengthValidator(1)],
        verbose_name="Тип найма сотрудника"
    )
    is_selected = models.BooleanField(
        default=False,
        verbose_name="Признак выбранного значения типа найма"
    )

    def __str__(self):
        return f"{self.name} (Selected: {'Yes' if self.is_selected else 'No'})"

    class Meta:
        db_table = 'employee_hire_types'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_employee_hire_type_name')
        ]


class Employees(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Уникальный идентификатор сотрудника (PK)",
    )

    parent_employee = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Уникальный идентификатор руководителя сотрудника (FK)"
    )
    password_hash = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(8),
        ],
        verbose_name="Хеш пароля пользователя"
    )
    first_name = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(1),
            RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ]+$', 'Only Latin or Cyrillic characters are allowed.')
        ],
        verbose_name="Имя сотрудника"
    )
    last_name = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(1),
            RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ]+$', 'Only Latin or Cyrillic characters are allowed.')
        ],
        verbose_name="Фамилия сотрудника"
    )

    patronymic = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        validators=[
            RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ]*$', 'Only Latin or Cyrillic characters are allowed.')
        ],
        verbose_name="Отчество сотрудника"
    )
    birth_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата рождения сотрудника с указанием временной зоны",
        validators=[employee_validate_birth_date]
    )

    position = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(1),
            RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ\s-]+$',
                           'Only Latin or Cyrillic characters, spaces, and hyphens are allowed.')
        ],
        verbose_name="Должность сотрудника"
    )
    city = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(1),
            RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ\s.-]+$',
                           'Only Latin or Cyrillic characters, spaces, hyphens, and dots are allowed.')
        ],
        verbose_name="Город проживания сотрудника"
    )
    country = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(1),
            RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ\s.-]+$',
                           'Only Latin or Cyrillic characters, spaces, hyphens, and dots are allowed.')
        ],
        verbose_name="Страна проживания сотрудника"
    )
    email = models.EmailField(
        max_length=254,
        validators=[MinLengthValidator(5)],
        verbose_name="Электронная почта пользователя",
        unique=True
    )
    phone = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(7),
            RegexValidator(r'^[0-9+\(\)\-\s]+$', 'Only digits, plus, parentheses, hyphens, and spaces are allowed.')
        ],
        verbose_name="Номер телефона"
    )
    telegram = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(5),
            RegexValidator(r'^@[0-9a-zA-Z_]+$',
                           'Telegram username must start with @ and can contain letters, numbers, and underscores.')
        ],
        verbose_name="Имя пользователя в телеграмм"
    )
    foto = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        validators=[MinLengthValidator(5)],
        verbose_name="Ссылка на фото профиля пользователя"
    )
    personal_information = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name="Дополнительная информация о сотруднике"
    )
    skills = JSONField(models.CharField(max_length=64), )

    vacation = models.ManyToManyField(
        Vacations,
        verbose_name="Уникальный идентификатор отпуска (FK)"
    )

    department = models.ForeignKey(
        Departments,
        on_delete=models.CASCADE,
        verbose_name="Уникальный идентификатор отдела (FK)",
        related_name='employees'
    )

    time_zone = models.ForeignKey(
        TimeZones,
        on_delete=models.CASCADE,
        verbose_name="Уникальный идентификатор временной зоны (FK)"
    )
    hire_at = models.DateTimeField(
        verbose_name="Дата найма сотрудника",
    )
    update_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата вносимых изменений в профиль сотрудника"
    )
    dismiss_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата увольнения сотрудника"
    )

    status = models.ForeignKey(
        EmployeeStatuses,
        on_delete=models.CASCADE,
        verbose_name="Уникальный идентификатор статуса сотрудника (FK)"
    )
    hire_type = models.ForeignKey(
        EmployeeHireTypes,
        on_delete=models.CASCADE,
        verbose_name="Уникальный идентификатор типа найма сотрудника (FK)"
    )

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return self.email


class KPIValue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True,
                          verbose_name='Уникальный идентификатор  (PK)')
    name = models.CharField(max_length=64, verbose_name='Название метрики')

    class Meta:
        db_table = 'kpi_values'


class ProjectStatuses(models.Model):
    STATUS_NOT_STARTED = 'not_started'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = [
        (STATUS_NOT_STARTED, 'Не начато'),
        (STATUS_IN_PROGRESS, 'В процессе'),
        (STATUS_COMPLETED, 'Выполнено'),
    ]
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True,
                          verbose_name='Уникальный идентификатор статуса (PK)')
    name = models.CharField(
        max_length=64,
        choices=STATUS_CHOICES,
        validators=[MinLengthValidator(1)],
        verbose_name="Название статуса"
    )
    is_selected = models.BooleanField(default=False,
                                      verbose_name="Признак выбранного значения статуса"
                                      )

    class Meta:
        db_table = 'project_statuses'
        ordering = ('name',)
        verbose_name = 'Статус проекта'
        verbose_name_plural = 'Статусы проектов'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_project_status_name')
        ]

    def __str__(self):
        return self.name


class ProjectPriorities(models.Model):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

    PRIORITY_CHOICES = [
        (HIGH, 'Высокий'),
        (MEDIUM, 'Средний'),
        (LOW, 'Низкий'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True,
                          verbose_name='Уникальный идентификатор приоритета (PK)')
    name = models.CharField(max_length=64, choices=PRIORITY_CHOICES, blank=True, null=True)
    is_selected = models.BooleanField(
        default=False,
        verbose_name="Признак выбранного значения статуса"
    )

    class Meta:
        db_table = 'project_priorities'
        ordering = ('name',)
        verbose_name = 'Приоритет проекта'
        verbose_name_plural = 'Приоритеты проекта'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_project_priority_name')
        ]

    def __str__(self):
        return self.name


class Links(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64, blank=True, null=True, unique=True)
    url = models.URLField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        db_table = 'links'


class Projects(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Уникальный идентификатор проекта (PK)"
    )
    parent_project = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Уникальный идентификатор головного проекта (FK)"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название проекта"
    )
    start_date = models.DateTimeField(
        verbose_name="Дата начала проекта"
    )
    end_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата окончания проекта"
    )
    short_description = models.TextField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name="Дополнительная информация о проекте, которая содержится в блоке «Описание проекта»"
    )
    comment = models.TextField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name="Дополнительная информация о проекте, которая содержится в блоке «Комментарии»"
    )
    kpi = models.ManyToManyField(KPIValue, through='ProjectKpiThrough', related_name='projects')

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания проекта"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата внесения изменений в проект"
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата удаления проекта"
    )
    status = models.ForeignKey(
        ProjectStatuses,
        on_delete=models.CASCADE,
        verbose_name="Уникальный идентификатор статусов проекта (FK)"
    )
    priorities = models.ForeignKey(
        ProjectPriorities,
        on_delete=models.CASCADE,
        verbose_name="Уникальный идентификатор приоритетов проекта (FK)"
    )
    links = models.ManyToManyField(
        Links,
    )
    participant = models.ManyToManyField(Employees, through='Participants', related_name='projects')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'projects'
        ordering = ('title',)
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectKpiThrough(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project_kpi')
    kpi = models.ForeignKey(KPIValue, on_delete=models.CASCADE, related_name='project_kpi')
    value = models.IntegerField(verbose_name='Значение метрики',
                                validators=[
                                    MinValueValidator(1),
                                    MaxValueValidator(1000000)
                                ])
    measured_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')

    class Meta:
        unique_together = ('project', 'kpi')

    def __str__(self):
        return f'{self.project} - {self.kpi}- {self.value}'


class Participants(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project_employee')
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='project_employee')
    is_working = models.BooleanField(default=False)

    class Meta:
        db_table = 'participants'
        unique_together = ('project', 'employee')

    def __str__(self):
        return f'Project {self.project} - Employee {self.employee} (Working: {self.is_working})'
