from rest_framework import routers
from attendance.views import InOutLogView, AttendanceSheetView
from attendance.admin_views import ShiftAdminView

router = routers.DefaultRouter()
router.register(r'in-out-log', InOutLogView, basename='in-out-log')
router.register(r'admin/attendance-sheet', AttendanceSheetView, basename='attendance-sheet')
router.register(r'admin/shift', ShiftAdminView, basename='shift')
urlpatterns = router.urls
