from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from fms.models import Post
from django.utils import timezone
from datetime import timedelta

class ShareLink(models.Model):
    token = models.CharField(max_length=100, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(User, related_name='shared_links', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='received_links')
    expiration_time = models.DateTimeField()

    def has_expired(self):
        return timezone.now() > self.expiration_time

    def __str__(self):
        return f"{self.shared_by.username} shared {self.post.title} with {self.shared_with.all()}"
