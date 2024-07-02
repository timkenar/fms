from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'file_path', 'date_created', 'date_updated']



#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user

#     def update(self, instance, validated_data):
#         password = validated_data.pop('password', None)
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         if password:
#             instance.set_password(password)
#         instance.save()
#         return instance

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'user', 'title', 'description', 'file_path', 'date_created', 'date_updated']

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     data['user'] = user
#                 else:
#                     raise serializers.ValidationError('User account is disabled.')
#             else:
#                 raise serializers.ValidationError('Unable to log in with provided credentials.')
#         else:
#             raise serializers.ValidationError('Must include "username" and "password".')

#         return data
