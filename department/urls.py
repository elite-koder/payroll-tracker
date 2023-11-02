from rest_framework import routers
from department.admin_views import DepartmentCreateAdminView, DepartmentListAdminView

router = routers.DefaultRouter()
router.register(r'admin/department/create', DepartmentCreateAdminView, 'department')
router.register(r'admin/department/list', DepartmentListAdminView, 'department')
urlpatterns = router.urls