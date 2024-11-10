from datetime import timedelta
from django.db import models
from django.utils import timezone
# Create your models here.


class Story (models.Model):
    image = models.ImageField(upload_to="user_story/", blank=False)
    caption = models.TextField(blank=True, max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Ensure `created_at` is set to `timezone.now()` if not already set
        if not self.created_at:
            self.created_at = timezone.now()

        if not self.expires_at:
            self.expires_at = self.created_at + timedelta(hours=24)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Story created at {self.created_at}"