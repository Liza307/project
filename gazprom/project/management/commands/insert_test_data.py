import datetime
import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from project.models import (
    TimeZones, Departments, Vacations, EmployeeStatuses, EmployeeHireTypes,
    Employees, KPIValue, ProjectStatuses, ProjectPriorities, Links,
    Projects, ProjectKpiThrough, Participants
)
fake = Faker()

class Command(BaseCommand):
    help = 'Insert test data into the database'

    def handle(self, *args, **kwargs):
        self.insert_time_zones()
        self.insert_departments()
        self.insert_vacations()
        self.insert_employee_statuses()
        self.insert_employee_hire_types()
        self.insert_employees()
        self.insert_kpi_values()
        self.insert_project_statuses()
        self.insert_project_priorities()
        self.insert_links()
        self.insert_projects()
        self.insert_participants()
        self.stdout.write(self.style.SUCCESS('Successfully inserted test data.'))

    def insert_time_zones(self):
        if   not TimeZones.objects.exists():

            time_zones = [
                {'name': 'UTC', 'abbrev': 'UTC', 'utc_offset': '+00:00'},
                {'name': 'New York', 'abbrev': 'EST', 'utc_offset': '-05:00'},
                {'name': 'Tokyo', 'abbrev': 'JST', 'utc_offset': '+09:00'}
            ]
            for tz in time_zones:
                TimeZones.objects.create(**tz)

    def insert_departments(self):
        if not Departments.objects.exists():
            num_departments = 5

            for _ in range(num_departments):
                random_title = fake.unique.company()
                count_employee = random.randint(1, 100)
                count_project = random.randint(1, 20)

                existing_departments = list(Departments.objects.all())
                random_parent = random.choice(existing_departments) if existing_departments else None

                Departments.objects.create(
                    title=random_title,
                    count_employee=count_employee,
                    count_project=count_project,
                    parent_department=random_parent
                )
    def insert_vacations(self):
        vacations = [
            {'start_date': timezone.now() - datetime.timedelta(days=10), 'end_date': timezone.now()},
            {'start_date': timezone.now() - datetime.timedelta(days=30),
             'end_date': timezone.now() - datetime.timedelta(days=20)},
            {'start_date': timezone.now() - datetime.timedelta(days=60),
             'end_date': timezone.now() - datetime.timedelta(days=50)}
        ]
        for vac in vacations:
            Vacations.objects.create(**vac)

    def insert_employee_statuses(self):
        if not EmployeeStatuses.objects.exists():

            statuses = [
                {'name': 'active', 'is_selected': True},
                {'name': 'inactive', 'is_selected': False},
                {'name': 'on_vacation', 'is_selected': False}
            ]
            for status in statuses:
                EmployeeStatuses.objects.create(**status)

    def insert_employee_hire_types(self):
        if not EmployeeHireTypes.objects.exists():
            hire_types = [
                {'name': 'Штатный', 'is_selected': True},
                {'name': 'Аутсорс', 'is_selected': False}
            ]
            for hire_type in hire_types:
                EmployeeHireTypes.objects.create(**hire_type)

    def insert_employees(self):
        for _ in range(20):
            first_name = fake.first_name()
            last_name = fake.last_name()
            patronymic = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            telegram = f'@{fake.user_name()}'
            foto = fake.image_url()
            personal_information = fake.sentence()
            city = fake.city()
            country = fake.country()
            position= fake.job()
            department = Departments.objects.order_by('?').first()
            time_zone = TimeZones.objects.order_by('?').first()
            status = EmployeeStatuses.objects.order_by('?').first()
            hire_type = EmployeeHireTypes.objects.order_by('?').first()

            hire_at = timezone.now() - datetime.timedelta(days=fake.random_int(min=30, max=500))
            all_employees = list(Employees.objects.all())
            parent_employee = fake.random_element(elements=all_employees + [None])
            Employees.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                telegram=telegram,
                foto=foto,
                personal_information=personal_information,
                city=city,
                country=country,
                department=department,
                time_zone=time_zone,
                hire_at=hire_at,
                status=status,
                hire_type=hire_type,
                parent_employee=parent_employee,
                patronymic=patronymic,
                position=position,
            )

    def insert_kpi_values(self):
        kpi_values = [
            {'name': 'Revenue'},
            {'name': 'Customer Satisfaction'},
            {'name': 'Employee Engagement'}
        ]
        for kpi in kpi_values:
            KPIValue.objects.create(**kpi)

    def insert_project_statuses(self):
        statuses = [
            {'name': 'not_started', 'is_selected': True},
            {'name': 'in_progress', 'is_selected': False},
            {'name': 'completed', 'is_selected': False}
        ]
        for status in statuses:
            ProjectStatuses.objects.create(**status)

    def insert_project_priorities(self):
        priorities = [
            {'name': 'high', 'is_selected': True},
            {'name': 'medium', 'is_selected': False},
            {'name': 'low', 'is_selected': False}
        ]
        for priority in priorities:
            ProjectPriorities.objects.create(**priority)

    def insert_links(self):
        links = [
            {'name': 'Documentation', 'url': 'http://example.com/doc'},
            {'name': 'GitHub', 'url': 'http://github.com/example'},
            {'name': 'Jira', 'url': 'http://jira.example.com'}
        ]
        for link in links:
            Links.objects.create(**link)

    def insert_projects(self):
        if not Projects.objects.exists():
            num_projects = 5

            for _ in range(num_projects):
                random_title = fake.unique.word().capitalize()  # Randomized title
                random_start_date = timezone.now() - datetime.timedelta(days=random.randint(30, 90))
                random_end_date = random_start_date + datetime.timedelta(days=random.randint(10, 40))
                if random_end_date > timezone.now():
                    random_end_date = None

                project_data = {
                    'title': random_title,
                    'start_date': random_start_date,
                    'end_date': random_end_date,
                    'short_description': fake.text(max_nb_chars=200),
                    'comment': fake.text(max_nb_chars=100),
                    'status': ProjectStatuses.objects.order_by('?').first(),
                    'priorities': ProjectPriorities.objects.order_by('?').first()
                }

                proj = Projects.objects.create(**project_data)

                proj.links.set(Links.objects.all())

                for kpi in KPIValue.objects.all():
                    ProjectKpiThrough.objects.create(
                        project=proj,
                        kpi=kpi,
                        value=random.randint(1, 100),
                        measured_at=timezone.now()
                    )

                existing_projects = list(Projects.objects.all())
                if existing_projects:
                    parent_project = random.choice(existing_projects)
                    proj.parent_project = parent_project
                    proj.save()
    def insert_participants(self):
        projects = Projects.objects.all()
        employees = Employees.objects.all()
        for project in projects:
            for employee in employees:
                Participants.objects.create(project=project, employee=employee, is_working=bool(random.getrandbits(1)))
