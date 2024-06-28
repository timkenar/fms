from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from fms.views import UserViewSet, PostViewSet, AuthViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'posts', PostViewSet)
router.register(r'auth', AuthViewSet,basename='auth')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('fms.urls'))


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


