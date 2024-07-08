from rest_framework import serializers
from fms.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'file_path', 'date_created', 'date_updated']
