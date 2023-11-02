from rest_framework import serializers
from department.models import Department
from user.serializers import UserReadSerializer

class DepartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'org')


class DepartmentUpdateManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'manager')

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

class ManagerReadSerializer(serializers.ModelSerializer):
    user = UserReadSerializer()
    class Meta:
        from employee.models import Employee
        model = Employee
        fields = ('id', 'user', 'mobile', 'level', 'profile_pic', 'status', 'dob', 'doj')


class DepartmentReadSerializer(serializers.ModelSerializer):
    manager = ManagerReadSerializer()
    class Meta:
        model = Department
        fields = ('id', 'name', 'manager')


class DepartmentListSerializer(serializers.ModelSerializer):
    manager = ManagerReadSerializer()
    class Meta:
        model = Department
        fields = ('id', 'name', 'manager')