from rest_framework import routers
from reimbursement.views import ExpenseClaimView, ExpenseClaimReviewUpdateView

router = routers.DefaultRouter()
router.register(r'expense-claim', ExpenseClaimView, basename='expense-claim-create')
router.register(r'expense-claim/review-update', ExpenseClaimReviewUpdateView, basename='expense-claim-review')
urlpatterns = router.urls