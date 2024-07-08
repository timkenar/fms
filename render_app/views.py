from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from fms.models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', 'date_created', 'user']
    search_fields = ['title', 'description']
    ordering_fields = ['date_created', 'title']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(user=user)
