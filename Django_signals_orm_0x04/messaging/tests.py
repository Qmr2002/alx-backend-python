from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessagingSignalsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='sender', password='testpass123')
        self.user2 = User.objects.create_user(username='receiver', password='testpass123')

    def test_notification_created_on_message_send(self):
        message = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello!")
        notification = Notification.objects.get(user=self.user2)

        self.assertEqual(notification.message, message)
        self.assertFalse(notification.is_read)
        self.assertEqual(notification.user, self.user2)
