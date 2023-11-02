from rest_framework import serializers
from leave.models import Leave

class LeaveCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ('id', 'employee', 'type', 'from_date', 'to_date', 'reason')

class LeaveReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ('id', 'employee', 'type', 'from_date', 'to_date', 'reason', 'status')

class LeaveDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave

    def destroy(self, instance):
        # validate that user deleting it's own leave
        return super().destroy(instance)

class LeaveReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ('id', 'status')

    def update(self, instance, validated_data):
        # validate for department manager
        return super().update(instance, validated_data)