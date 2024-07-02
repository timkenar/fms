from rest_framework import serializers
from .models import ShareLink
from fms.models import Post
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class ShareLinkSerializer(serializers.ModelSerializer):
    shared_with = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = ShareLink
        fields = ['id', 'token', 'post', 'shared_by', 'shared_with', 'expiration_time']

    def create(self, validated_data):
        shared_with = validated_data.pop('shared_with')
        validated_data['expiration_time'] = datetime.now() + timedelta(hours=1)  # Example: link expires after 1 hour
        share_link = ShareLink.objects.create(**validated_data)
        share_link.shared_with.set(shared_with)
        return share_link
