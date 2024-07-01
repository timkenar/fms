from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

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













# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.models import User
# from .models import Post
# from .serializers import UserSerializer, PostSerializer, LoginSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_superuser:
#             return Post.objects.all()
#         return Post.objects.filter(user=user)

#     @action(detail=False, methods=['post'])
#     def save_post(self, request):
#         data = request.data
#         post_id = data.get('id')
#         if post_id:
#             post = Post.objects.get(id=post_id)
#             serializer = PostSerializer(post, data=data)
#         else:
#             serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 'success', 'msg': 'File has been saved successfully.'}, status=status.HTTP_200_OK)
#         return Response({'status': 'failed', 'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     @action(detail=False, methods=['post'])
#     def delete_post(self, request):
#         post_id = request.data.get('id')
#         try:
#             post = Post.objects.get(id=post_id)
#             post.delete()
#             return Response({'status': 'success', 'msg': 'Post has been deleted successfully'}, status=status.HTTP_200_OK)
#         except Post.DoesNotExist:
#             return Response({'status': 'failed', 'msg': 'Undefined Post ID'}, status=status.HTTP_400_BAD_REQUEST)

# class LoginViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=['post'])
#     def login(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             login(request, user)
#             return Response({'status': 'success'}, status=status.HTTP_200_OK)
#         return Response({'status': 'failed', 'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     @action(detail=False, methods=['post'])
#     def logout(self, request):
#         logout(request)
#         return Response({'status': 'success'}, status=status.HTTP_200_OK)

#     @action(detail=False, methods=['post'])
#     def register(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             user = authenticate(username=serializer.data['username'], password=request.data['password'])
#             if user:
#                 login(request, user)
#                 return Response({'status': 'success'}, status=status.HTTP_200_OK)
#         return Response({'status': 'failed', 'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
