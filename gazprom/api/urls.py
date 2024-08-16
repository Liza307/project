from api.views import ProjectViewSet, EmployeeViewSet, DepartmentsViewSet, StructureViewSet, UserViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('structure', StructureViewSet)
router.register('projects', ProjectViewSet)
router.register('employees', EmployeeViewSet)
router.register('departments', DepartmentsViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
