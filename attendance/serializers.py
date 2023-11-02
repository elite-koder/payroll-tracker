from rest_framework import serializers
from attendance.models import AttendanceRegister, InOutLog, Shift
from django.utils import timezone

class InOutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InOutLog
        read_only_fields = ('in_out_dt', 'created_on')
        fields = ('id', 'in_out', 'in_out_dt', 'created_on')

    def create(self, validated_data):
        validated_data['employee'] = self.context['request'].user.employee
        return super().create(validated_data)
    

class AttendanceRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRegister
        fields = ('id', 'employee', 'day', 'created_on')


class AttendanceSheetRequestSerializer(serializers.Serializer):
    month = serializers.IntegerField(min_value=1, max_value=12)
    year = serializers.IntegerField(min_value=1972, max_value=2972)


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        read_only_fields = ('id', 'created_on', 'modified_on')
        fields = ('id', 'name', 'start_time', 'end_time', 'grace_in', 'grace_out', 'created_on', 'modified_on')