from rest_framework.routers import DefaultRouter

from .views import OrderViewSet


router = DefaultRouter()
router.register(r'list', OrderViewSet)
urlpatterns = router.urls