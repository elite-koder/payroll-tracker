from rest_framework import mixins, viewsets
from employee.models import Employee
from employee.serializers import EmployeeCreateSerializer, EmployeeReadSerializer
from rest_framework.parsers import MultiPartParser

class EmployeeCreateAdminView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EmployeeCreateSerializer
    parser_classes = (MultiPartParser, )
    queryset = Employee.objects.all()


class EmployeeListAdminView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = EmployeeReadSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveAdminView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = EmployeeReadSerializer
    queryset = Employee.objects.all()
