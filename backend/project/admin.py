from django.contrib import admin
from .models import (TimeZones,
                     Departments,
                     Vacations,
                     EmployeeStatuses,
                     EmployeeHireTypes,
                     Employees,
                     KPIValue,
                     ProjectStatuses,
                     ProjectPriorities,
                     Links,
                     Projects,
                     ProjectKpiThrough,
                     Participants)

@admin.register(TimeZones)
class TimeZonesAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbrev', 'utc_offset')
    search_fields = ('name', 'abbrev')
    ordering = ('name',)

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_employee', 'count_project', 'parent_department')
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(Vacations)
class VacationsAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date')
    search_fields = ('start_date', 'end_date')
    ordering = ('start_date',)

@admin.register(EmployeeStatuses)
class EmployeeStatusesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_selected')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(EmployeeHireTypes)
class EmployeeHireTypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_selected')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'department', 'email', 'status', 'hire_type')
    search_fields = ('first_name', 'last_name', 'email', 'department__title', 'status__name', 'hire_type__name')
    list_filter = ('department', 'status', 'hire_type', 'time_zone')
    ordering = ('last_name', 'first_name')

@admin.register(KPIValue)
class KPIValueAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(ProjectStatuses)
class ProjectStatusesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_selected')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(ProjectPriorities)
class ProjectPrioritiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_selected')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'url')
    ordering = ('name',)

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status', 'priorities', 'created_at', 'updated_at')
    search_fields = ('title', 'short_description', 'comment', 'status__name', 'priorities__name')
    list_filter = ('status', 'priorities', 'links')
    ordering = ('title',)

@admin.register(ProjectKpiThrough)
class ProjectKpiThroughAdmin(admin.ModelAdmin):
    list_display = ('project', 'kpi', 'value', 'measured_at')
    search_fields = ('project__title', 'kpi__name')
    list_filter = ('project', 'kpi')
    ordering = ('project', 'kpi')

@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('project', 'employee', 'is_working')
    search_fields = ('project__title', 'employee__first_name', 'employee__last_name')
    list_filter = ('project', 'employee', 'is_working')
    ordering = ('project', 'employee')
