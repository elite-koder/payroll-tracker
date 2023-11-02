from rest_framework import serializers
from django.db import transaction
from employee.models import Employee
from user.serializers import UserCreateSerializer, UserReadSerializer
from organization.serializers import OrgReadSerializer
from department.serializers import DepartmentReadSerializer
from designation.serializers import DesignationReadSerializer


class EmployeeCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        model = Employee
        fields = ('id', 'user', 'mobile', 'department', 'designation', 'level', 'profile_pic', 'status', 'dob', 'doj', 'pan_number', 'aadhar_number', 'created_on', 'modified_on', 'org')

    def create(self, validated_data):
        with transaction.atomic():
            validated_data['user'] = UserCreateSerializer().create(validated_data.pop('user'))
            return super().create(validated_data)


class EmployeeReadSerializer(serializers.ModelSerializer):
    user = UserReadSerializer()
    org = OrgReadSerializer()
    department = DepartmentReadSerializer()
    designation = DesignationReadSerializer()
    class Meta:
        model = Employee
        fields = ('id', 'user', 'department', 'designation', 'level', 'profile_pic', 'status', 'dob', 'doj', 'pan_number', 'aadhar_number', 'created_on', 'modified_on', 'org')


