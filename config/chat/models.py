# models.py

from django.db import models
from accounts.models import Account

class Message(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='received_messages')
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.recipient.username}: {self.message_text[:20]}..."
