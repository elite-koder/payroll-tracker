from rest_framework import routers
from designation.admin_views import DesignationCreateAdminView, DesignationListAdminView

router = routers.DefaultRouter()
router.register('admin/designation/create', DesignationCreateAdminView, 'designation')
router.register('admin/designation/list', DesignationListAdminView, 'designation')

urlpatterns = router.urls
