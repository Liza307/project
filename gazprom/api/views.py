from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from project.models import (Departments,
                            Employees,
                            Projects,
                            Participants)
from .serializers import (StructureGetSerializer,
                          EmployeeDetailGetSerializer,
                          DepartmentProjectsDetailGetSerializer,
                          DepartmentEmployeeDetailGetSerializer,
                          ProjectExtendedDetailSerializer
                          )


class CompanyStructureView(APIView):
    'api/v1/structure/company'

    def get(self, request):
        top_level_departments = Departments.objects.all()
        all_employees = Employees.objects.all()

        data = {
            'departments': top_level_departments,
            'employees': all_employees
        }

        serializer = StructureGetSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeListView(APIView):
    'api/v1/employees/list/'

    def get(self, request):
        all_employees = Employees.objects.all()
        serializer = EmployeeDetailGetSerializer(all_employees, many=True)
        return Response({'employees': serializer.data}, status=status.HTTP_200_OK)


class ProjectsListView(APIView):
    'api/v1/projects'

    def get(self, request, ):
        serializer = ProjectExtendedDetailSerializer(Projects.objects.all(), many=True)
        return Response({'projects': serializer.data}, status=status.HTTP_200_OK)


class DepartmentEmployeeListView(APIView):
    'api/v1/departments/{departmentId}/employees'

    def get(self, request, department_id):
        try:
            department = Departments.objects.get(pk=department_id)
        except Departments.DoesNotExist:
            return Response({"detail": "Department not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentEmployeeDetailGetSerializer(department, many=False)
        return Response({'departments': serializer.data}, status=status.HTTP_200_OK)


class DepartmentProjectListView(APIView):
    'api/v1/departments/{departmentId}/projects'

    def get(self, request, department_id):
        try:
            department = Departments.objects.get(pk=department_id)
        except Departments.DoesNotExist:
            return Response({"detail": "Department not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentProjectsDetailGetSerializer(department, many=False)
        return Response({'departments': serializer.data}, status=status.HTTP_200_OK)
