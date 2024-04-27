from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, Account, LoginSerializer

from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status



class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer



class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # Login successful, return token or user data

            user_serializer = UserSerializer(user)
            return Response({

                'user': user_serializer.data
            }, status=status.HTTP_200_OK)

        else:
            # Login failed
            return Response({
                'error': 'Login yoki parol xato!'
            }, status=status.HTTP_401_UNAUTHORIZED)
