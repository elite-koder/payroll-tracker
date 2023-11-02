from rest_framework import viewsets, mixins
from leave.serializers import LeaveCreateSerializer, LeaveReadSerializer, LeaveReviewUpdateSerializer, LeaveDestroySerializer
from leave.models import Leave

class LeaveCreateView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LeaveCreateSerializer
    queryset = Leave.objects.all()
    

class LeaveListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = LeaveReadSerializer
    queryset = Leave.objects.all()


class LeaveDeleteView(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = LeaveDestroySerializer
    queryset = Leave.objects.all()

    def get_queryset(self):
        # check if user deleting it's own leave
        return super().get_queryset()


class LeavePendingReviewListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    # filter all leaves where current logged in user is 
    # department manager of leave request employee and status is pending
    serializer_class = LeaveReadSerializer
    queryset = Leave.objects.all()
    def get_queryset(self):
        return super().get_queryset().filter(status="Pending")
    
class LeaveReviewUpdateView(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = LeaveReviewUpdateSerializer
    queryset = Leave.objects.all()