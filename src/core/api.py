from rest_framework import routers
from .views import ContentViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename="user")
router.register('content', ContentViewSet, basename="content")