from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Message, MessageHistory
from django.contrib.auth.models import User


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Message.objects.get(pk=instance.pk)
        if old_instance.content != instance.content:
            MessageHistory.objects.create(
                message=instance,
                old_content=old_instance.content
            )
            instance.edited = True  # Mark the message as edited

@receiver(post_delete, sender=User)
def clean_up_user_related_data(sender, instance, **kwargs):
    # Delete messages (sent or received)
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete notifications
    Notification.objects.filter(user=instance).delete()

    # Delete message histories for messages that were edited by this user
    MessageHistory.objects.filter(edited_by=instance).delete()