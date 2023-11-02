from rest_framework import viewsets
from designation.models import Designation
from designation.serializers import DesignationCreateSerializer, DesignationReadSerializer

class DesignationCreateAdminView(viewsets.ModelViewSet):
    serializer_class = DesignationCreateSerializer
    queryset = Designation.objects.all()

class DesignationListAdminView(viewsets.ModelViewSet):
    serializer_class = DesignationReadSerializer
    queryset = Designation.objects.all()