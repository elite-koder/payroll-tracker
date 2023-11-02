from rest_framework import routers
from leave.views import LeaveCreateView, LeaveListView, LeavePendingReviewListView, LeaveReviewUpdateView, LeaveDeleteView

router = routers.DefaultRouter()
router.register("leave/create", LeaveCreateView, "leave")
router.register("leave/list", LeaveListView, "leave")
router.register("leave/pending-review-list", LeavePendingReviewListView, "leave")
router.register("leave/review-update", LeaveReviewUpdateView, "leave")
router.register("leave/delete", LeaveDeleteView, "leave")
urlpatterns = router.urls