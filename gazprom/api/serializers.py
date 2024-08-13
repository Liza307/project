from django.contrib.auth import get_user_model
from project.models import (
    Departments,
    Employee,
    KPI_values,
    Priority,
    Project,
    Time_zones,
    Vacations,
)

# from django.core.exceptions import ValidationError
# from djoser.serializers import UserCreateSerializer, UserSerializer
# from drf_base64.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

User = get_user_model()


class PrioritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Priority

    #    fields = ('id', 'name', 'measurement_unit')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project

    #   fields = ('id', 'name', 'color', 'slug')


# class UserReadSerializer(UserSerializer):
#   is_subscribed = serializers.SerializerMethodField(read_only=True)

#   class Meta:
#       model = User
#       fields = (
#          'email',
#          'id',
#           'username',
#           'first_name',
#          'last_name',
#           'is_subscribed',
#       )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        # fields = ('id', 'name', 'measurement_unit', 'amount')
        model = Employee


class DepartmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments

    #    fields = (
    #        'id',
    #    )


class VacationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacations


#       fields = (
#          'tags',
#       )

#    def validate_cooking_time(self, value):
#      if value < 1:
#           raise ValidationError('Время не может быть меньше 1')
#       return value


class Time_zonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_zones

    #   fields = ('user', 'author')


class KPI_valuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPI_values

    #   fields = (
    #       'email',
    #      'username',


#     )


# class ShortRecipeGetSerializer(serializers.ModelSerializer):
#    """Краткое отображение рецепта"""

#   image = Base64ImageField(required=True, allow_null=False)

# class Meta:
#       model = Recipe
#       fields = (
#          'id',
#         'name',
#          'image',
#          'cooking_time',
#      )
