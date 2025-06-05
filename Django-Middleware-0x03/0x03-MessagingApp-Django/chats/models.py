import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# 🔹 1. Custom User Model
class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=128, verbose_name='password')

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

# 🔹 2. Conversation Model
class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    participants = models.ManyToManyField(User, related_name='conversations')
    is_group = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"Conversation {self.conversation_id}"

# 🔹 3. Message Model
class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.sent_at}"

