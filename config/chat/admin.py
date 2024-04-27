from django.contrib import admin
from .models import Message
# Register your models here.
from django.contrib.admin import ModelAdmin

@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'message_text', 'created_at')

    ordering = ('-created_at', )
    search_fields = ('id', 'sender')
