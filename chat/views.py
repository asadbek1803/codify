from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Message

def chat(request, recipient_username):
    recipient = get_object_or_404(User, username=recipient_username)
    messages = Message.objects.filter(
        sender=request.user, recipient=recipient
    ) | Message.objects.filter(
        sender=recipient, recipient=request.user
    )
    messages = messages.order_by('created_at')

    if request.method == 'POST':
        message_text = request.POST.get('message')
        Message.objects.create(
            sender=request.user,
            recipient=recipient,
            message_text=message_text
        )

    context = {
        'recipient': recipient,
        'messages': messages,
    }
    return render(request, 'chat/chat.html', context)