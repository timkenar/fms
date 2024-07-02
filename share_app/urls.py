from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShareLinkViewSet

router = DefaultRouter()
router.register(r'share_links', ShareLinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
