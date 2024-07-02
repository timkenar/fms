from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ShareLink
from .serializers import ShareLinkSerializer
from fms.models import Post
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string

class ShareLinkViewSet(viewsets.ModelViewSet):
    queryset = ShareLink.objects.all()
    serializer_class = ShareLinkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        token = get_random_string(20)
        serializer.save(token=token, shared_by=self.request.user)

    @action(detail=True, methods=['get'])
    def validate_link(self, request, pk=None):
        try:
            share_link = ShareLink.objects.get(pk=pk)
            if share_link.has_expired():
                return Response({'status': 'failed', 'msg': 'Link has expired'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'status': 'success', 'post': share_link.post.id}, status=status.HTTP_200_OK)
        except ShareLink.DoesNotExist:
            return Response({'status': 'failed', 'msg': 'Invalid link'}, status=status.HTTP_400_BAD_REQUEST)
