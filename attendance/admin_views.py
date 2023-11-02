from rest_framework import mixins, viewsets
from attendance.models import Shift
from attendance.serializers import ShiftSerializer
from rest_framework.permissions import IsAdminUser

class ShiftAdminView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ShiftSerializer
    queryset = Shift.objects.all()
    permission_classes = (IsAdminUser,)