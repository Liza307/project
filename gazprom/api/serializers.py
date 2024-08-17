from rest_framework import serializers
from project.models import (Employees,
                            Departments,
                            Projects,
                            Participants,
                            ProjectStatuses,
                            ProjectPriorities)


class EmployeeDetailGetSerializer(serializers.ModelSerializer):
    parentEmployeeId = serializers.SerializerMethodField()
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')

    class Meta:
        model = Employees
        fields = (
            'id',
            'parentEmployeeId',
            'firstName',
            'lastName',
            'patronymic',
            'position',
        )

    def get_parentEmployeeId(self, obj):
        return str(obj.parent_employee.id) if obj.parent_employee else None


class ParticipantDetailGetSerializer(serializers.ModelSerializer):
    projectId = serializers.SerializerMethodField()
    employeeId = serializers.SerializerMethodField()

    class Meta:
        model = Participants
        fields = ['projectId', 'employeeId']

    def get_projectId(self, obj):
        return str(obj.project.id)

    def get_employeeId(self, obj):
        return str(obj.employee.id)


class ProjectBaseDetailSerializer(serializers.ModelSerializer):
    parenProjectId = serializers.SerializerMethodField()
    participants = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = [
            'id',
            'parenProjectId',
            'title',
            'participants',
        ]

    def get_parenProjectId(self, obj):
        return str(obj.parent_project.id) if obj.parent_project else None

    def get_participants(self, obj):
        participants = Participants.objects.filter(project=obj)
        serializer = ParticipantDetailGetSerializer(participants, many=True)
        return serializer.data


class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatuses
        fields = ['name']


class ProjectPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPriorities
        fields = ['name']


class ProjectExtendedDetailSerializer(ProjectBaseDetailSerializer):
    status = serializers.SerializerMethodField()
    priorities = serializers.SerializerMethodField()

    class Meta(ProjectBaseDetailSerializer.Meta):
        model = Projects
        fields = ProjectBaseDetailSerializer.Meta.fields + [
            'status',
            'priorities',
        ]

    def get_status(self, obj):
        if obj.status:
            serializer = ProjectStatusSerializer(obj.status)
            return {'selected': serializer.data['name']}
        return {'selected': None}

    def get_priorities(self, obj):
        if obj.priorities:
            serializer = ProjectPrioritySerializer(obj.priorities)
            return {'selected': serializer.data['name']}
        return {'selected': None}

class DepartmentBaseDetailSerializer(serializers.ModelSerializer):
    parentDepartmentId = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    countEmployee = serializers.CharField(source='count_employee')
    countProject = serializers.CharField(source='count_project')

    class Meta:
        model = Departments
        fields = [
            'id',
            'parentDepartmentId',
            'title',
            'countEmployee',
            'countProject',
        ]

    def get_parentDepartmentId(self, obj):
        return str(obj.parent_department.id) if obj.parent_department else None


class DepartmentProjectsDetailGetSerializer(DepartmentBaseDetailSerializer):
    projects = serializers.SerializerMethodField()

    class Meta(DepartmentBaseDetailSerializer.Meta):
        model = Departments
        fields = DepartmentBaseDetailSerializer.Meta.fields + [
            'projects',
        ]

    def get_projects(self, obj):
        employees = Employees.objects.filter(department=obj)
        participants = Participants.objects.filter(employee__in=employees)
        projects = Projects.objects.filter(project_employee__in=participants).distinct()
        serializer = ProjectExtendedDetailSerializer(projects, many=True)
        return serializer.data


class DepartmentEmployeeDetailGetSerializer(DepartmentBaseDetailSerializer):
    employees = serializers.SerializerMethodField()

    class Meta(DepartmentBaseDetailSerializer.Meta):
        model = Departments
        fields = DepartmentBaseDetailSerializer.Meta.fields + [
            'employees',
        ]

    def get_employees(self, obj):
        employees = Employees.objects.filter(department=obj)
        serializer = EmployeeDetailGetSerializer(employees, many=True)
        return serializer.data


class StructureGetSerializer(serializers.Serializer):
    departments = DepartmentProjectsDetailGetSerializer(many=True, read_only=True)
    employees = EmployeeDetailGetSerializer(many=True, read_only=True)
