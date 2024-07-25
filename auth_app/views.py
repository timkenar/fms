from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

class AuthViewSet(viewsets.ViewSet):
    @csrf_exempt
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'status': 'success', 'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
            return Response({'status': 'failed', 'msg': 'Inactive user'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'failed', 'msg': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def logout(self, request):
        logout(request)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    @csrf_exempt
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'status': 'success', 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response({'status': 'failed', 'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def current_user(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
