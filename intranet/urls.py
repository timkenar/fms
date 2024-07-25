from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auth_app.urls')),
    #  path('api/', include('auth_app.urls')),
    path('api/fms/', include('fms.urls')),
    path('api/share/', include('share_app.urls')),
    path('api/notify/', include('notify_app.urls')),
    path('api/render/', include('render_app.urls')),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

