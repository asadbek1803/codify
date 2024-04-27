# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:recipient_username>/', views.chat, name='chat'),
    path('send_message/', views.send_message, name='send_message'),
    path('profile/<str:username>/', views.UserProfileView.as_view())
]