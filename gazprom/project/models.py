from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Status(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    color = ColorField(max_length=256, default='#00FF00', verbose_name='Цвет')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    color = ColorField(max_length=256, default='#00FF00', verbose_name='Цвет')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'

    def __str__(self):
        return self.name


class Project(models.Model):
    # parent_project_id
    title = models.CharField(max_length=255, verbose_name='Название проекта')
    start_date = models.DateTimeField(verbose_name='Дата начала проекта')
    end_date = models.DateTimeField(verbose_name='Дата окончания проекта')
    jira_link = models.URLField(
        max_length=255, verbose_name='Ссылка на проект Jira'
    )
    confluence_link = models.URLField(
        max_length=255, verbose_name='Ссы лка на проект в Confluence'
    )
    git_link = models.URLField(max_length=255, verbose_name='Ссылка на GitLab')
    status = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    short_description = models.TextField(verbose_name='Описание')
    comment = models.TextField(verbose_name='Описание')
    # kpi_id
    created_at = models.DateTimeField(verbose_name='Дата создания проекта')
    updated_at = models.DateTimeField(
        verbose_name='Дата внесения изменений в проект'
    )
    deleted_at = models.DateTimeField(verbose_name='Дата удаления проекта')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Employee(models.Model):
    # parent_emloyee_id
    first_name = models.CharField(
        max_length=64, verbose_name='Название отдела'
    )
    last_name = models.CharField(max_length=64, verbose_name='Название отдела')
    patronymic = models.CharField(
        max_length=64, verbose_name='Название отдела'
    )
    birth_date = models.DateTimeField(verbose_name='Дата рождения сотрудника')
    position = models.CharField(max_length=64, verbose_name='Название отдела')
    city = models.CharField(max_length=64, verbose_name='Название отдела')
    country = models.CharField(max_length=64, verbose_name='Название отдела')
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    # phone
    # telegram =
    # photo
    #  status
    #  hire_type
    personal_information = models.TextField(verbose_name='Описание')
    #  skills
    # vacation_id
    # department_id
    # time_zone_id
    hire_at = models.DateTimeField(verbose_name='Дата найма сотрудника')
    update_at = models.DateTimeField(verbose_name='Дата вносимых изменений')
    dismiss_at = models.DateTimeField(
        verbose_name='Дата увольнения сотрудника'
    )


class Departments(models.Model):
    # parent_department_id
    title = models.CharField(max_length=64, verbose_name='Название отдела')
    count_employee = models.IntegerField(
        verbose_name='Количество сотрудников в департаменте/отделе',
    )
    count_project = models.IntegerField(
        verbose_name='Количество проектов в департаменте/отделе',
    )


class Vacations(models.Model):
    start_date = models.DateTimeField(verbose_name='Дата начала отпуска')
    end_date = models.DateTimeField(verbose_name='Дата окончания отпуска')


class Time_zones(models.Model):
    name = models.CharField(
        max_length=64, verbose_name='Название часового пояса'
    )
    abbrev = models.CharField(
        max_length=5, verbose_name='Аббревиатура часового пояса'
    )
    utc_offset = models.CharField(
        max_length=5, verbose_name='Аббревиатура часового пояса'
    )


class KPI_values(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название метрики')
    value = models.IntegerField(
        verbose_name='Значение метрики',
    )
    measured_at = models.DateTimeField(verbose_name='Дата измерения')
