from django.urls import path
from .import views


urlpatterns = [
    path('users/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/save/', views.PostViewSet.as_view({'post': 'save_post'})),
    path('posts/delete/', views.PostViewSet.as_view({'post': 'delete_post'})),
    path('auth/login/', views.AuthViewSet.as_view({'post': 'login'})),
    path('auth/logout/', views.AuthViewSet.as_view({'post': 'logout'})),
    path('auth/register/', views.AuthViewSet.as_view({'post': 'register'})),
]