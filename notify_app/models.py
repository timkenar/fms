from django.db import models

# My models.

from django.contrib.auth.models import User
from django.utils import timezone

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:20]}..."
