from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post
from .serializers import UserSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(user=user)

    @action(detail=False, methods=['post'])
    def save_post(self, request):
        data = request.data
        post_id = data.get('id')
        if post_id:
            post = Post.objects.get(id=post_id)
            serializer = PostSerializer(post, data=data)
        else:
            serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'msg': 'File has been saved successfully.'}, status=status.HTTP_200_OK)
        return Response({'status': 'failed', 'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def delete_post(self, request):
        post_id = request.data.get('id')
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return Response({'status': 'success', 'msg': 'Post has been deleted successfully'}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'status': 'failed', 'msg': 'Undefined Post ID'}, status=status.HTTP_400_BAD_REQUEST)

class AuthViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            return Response({'status': 'failed', 'msg': 'Inactive user'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'failed', 'msg': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def register(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = authenticate(username=data['username'], password=data['password'])
            login(request, user)
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        return Response({'status': 'failed', 'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
