from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils import timezone
from project.models import Departments, Employee, Project

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    DepartmentsSerializer,
    EmployeeSerializer,
    ProjectSerializer,
)

User = get_user_model()


class StructureViewSet(ModelViewSet):

    @action(
    def company(self, request, pk):
        return


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
)

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = None


class DepartmentsViewSet(ModelViewSet):
    queryset = Departments.objects.all()
    #    filter_backends = (DjangoFilterBackend,)
    http_method_names = ('get', 'post', 'patch', 'delete')
