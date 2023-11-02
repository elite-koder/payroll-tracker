from rest_framework import mixins, viewsets
from reimbursement.serializers import ExpenseClaimCreateSerializer, ExpenseClaimReviewUpdateSerializer
from reimbursement.models import ExpenseClaim
from rest_framework.parsers import MultiPartParser

class ExpenseClaimView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = ExpenseClaimCreateSerializer
    queryset = ExpenseClaim.objects.all()
    parser_classes = (MultiPartParser, )

    def get_queryset(self):
        # only logged in user can see or delete their expense claims
        return super().get_queryset()
    
class ExpenseClaimReviewUpdateView(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ExpenseClaimReviewUpdateSerializer
    queryset = ExpenseClaim.objects.all()

    def get_queryset(self):
        # only respective manager can update expense claims
        return super().get_queryset()