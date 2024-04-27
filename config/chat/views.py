from accounts.models import Account
from django.shortcuts import render, get_object_or_404
from .models import Message
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Message
def chat(request, recipient_username):
    recipient = get_object_or_404(Account, username=recipient_username)
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
    return render(request, 'chat/index.html', context)


@login_required
def send_message(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient')
        message_text = request.POST.get('message')

        # Xabar qabul qiluvchini topish
        recipient = get_object_or_404(Account, id=recipient_id)

        # Xabar matnini tekshirish
        if message_text:
            # Xabar yaratish
            message = Message.objects.create(
                sender=request.user,
                recipient=recipient,
                text=message_text
            )
            messages.success(request, 'Xabar yuborildi!')
        else:
            messages.error(request, 'Xabar matni kiritilmagan!')

    return redirect('chat')

from django.views.generic import DetailView
from accounts.models import Account

class UserProfileView(DetailView):
    model = Account
    template_name = 'chat/profile.html'
    context_object_name = 'user_obj'
    slug_field = 'username'
    slug_url_kwarg = 'username'

