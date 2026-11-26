from pprint import pprint

from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserRegistrationSerializer,UserProfileSerializer
from django.conf import settings
from rest_framework.decorators import api_view

# Create your views here.


class UserRegistrationAPIView(CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserRegistrationSerializer
    permission_classes=[AllowAny]


class UserProfileAPIView(RetrieveUpdateAPIView):
    serializer_class=UserProfileSerializer
    def get_object(self):
        pprint(self.request.user)
        return self.request.user

# @api_view(['GET','PUT','PATCH'])
# def UserProfileView(request):
#     pprint(request.user)
#     return Response({'data':'it is working fine'},status=status.HTTP_200_OK)

