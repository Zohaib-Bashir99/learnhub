from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserRegistrationSerializer


# Create your views here.


class UserRegistrationAPIView(CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserRegistrationSerializer
    permission_classes=[AllowAny]

