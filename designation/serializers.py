from rest_framework import serializers
from designation.models import Designation

class DesignationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ('id', 'name', 'org')

class DesignationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ('id', 'name')