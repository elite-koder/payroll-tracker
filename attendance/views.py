from rest_framework import mixins, viewsets, generics
from attendance.serializers import InOutLogSerializer, AttendanceSheetRequestSerializer
from attendance.models import InOutLog
from rest_framework.response import Response
from django.utils import timezone

class InOutLogView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = InOutLogSerializer
    queryset = InOutLog.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(employee=self.request.user.employee)
    

class AttendanceSheetView(generics.ListAPIView, viewsets.GenericViewSet):
    def list(self, request, *args, **kwargs):
        serializer = AttendanceSheetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        month, year = serializer.validated_data['month'], serializer.validated_data['year']
        from_date = timezone.datetime(year=year, month=month, day=1).date()
        to_date = timezone.datetime(year=year, month=month+1, day=1).date() # not inclusive
        InOutLog.objects.filter(created_at__gte=from_date, created_at__lt=to_date).annotate()
        return Response({"message": "Hello, world!"})
        # return super().get(request, *args, **kwargs)