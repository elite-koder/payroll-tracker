from rest_framework import routers
from user.views import LoginView

router = routers.DefaultRouter()
router.register(r'login', LoginView, basename='login')
urlpatterns = router.urls