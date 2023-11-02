from rest_framework import mixins, viewsets
from department.serializers import DepartmentCreateSerializer, DepartmentListSerializer
from department.models import Department

class DepartmentCreateAdminView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = DepartmentCreateSerializer
    queryset = Department.objects.all()


class DepartmentListAdminView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DepartmentListSerializer
    queryset = Department.objects.all()