from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, LoginViewSet


router = DefaultRouter()

router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, basename='login')


urlpatterns = router.urls 

