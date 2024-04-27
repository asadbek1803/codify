from django.urls import path

from .views import LoginView, RegisterView
urlpatterns = [
    path('api/v1/login', LoginView.as_view(), name='login_api_for_app'),
    path('api/v1/signup', RegisterView.as_view(), name='signup_api_for_app')
]