from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CompanyStructureView,
                       EmployeeListView,
                       DepartmentEmployeeListView,
                       ProjectsListView,
                       DepartmentProjectListView
                       )

router = DefaultRouter()

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('structure/company/', CompanyStructureView.as_view()),
    path('employees/list/', EmployeeListView.as_view()),
    path('projects/', ProjectsListView.as_view()),
    path('departments/<uuid:department_id>/projects/', DepartmentProjectListView.as_view()),
    path('departments/<uuid:department_id>/employees/', DepartmentEmployeeListView.as_view()),

]

