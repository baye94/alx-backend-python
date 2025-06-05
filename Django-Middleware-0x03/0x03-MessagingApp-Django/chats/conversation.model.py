from django.conf import settings
from django.db import models

class Conversation(models.Model):
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='conversations'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    is_group = models.BooleanField(default=False)

    def __str__(self):
        if self.title:
            return self.title
        return f"Conversation #{self.id}"
