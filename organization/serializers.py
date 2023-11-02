from rest_framework import serializers
from organization.models import Organization

class OrgReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'email', 'website', 'logo', 'created_on', 'modified_on')