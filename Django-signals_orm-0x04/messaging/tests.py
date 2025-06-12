from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, MessageHistory

class MessageEditTrackingTest(TestCase):
    def test_edit_logs_history(self):
        user1 = User.objects.create_user(username='u1', password='pass')
        user2 = User.objects.create_user(username='u2', password='pass')
        msg = Message.objects.create(sender=user1, receiver=user2, content='Initial message')

        msg.content = 'Updated message'
        msg.save()

        self.assertEqual(MessageHistory.objects.count(), 1)
        history = MessageHistory.objects.first()
        self.assertEqual(history.old_content, 'Initial message')
        self.assertTrue(msg.edited)
