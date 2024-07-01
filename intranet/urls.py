from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.routers import DefaultRouter
#from .views import UserViewSet, PostViewSet, AuthViewSet
# router = DefaultRouter()
# router.register(r'auth', AuthViewSet, basename='auth')
# router.register(r'users', UserViewSet)
# router.register(r'posts', PostViewSet)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('', include('fms.urls'))


# ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth_app.urls')),
    path('api/fms/', include('fms.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

