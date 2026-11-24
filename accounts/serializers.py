from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):


    password = serializers.CharField(max_length=128,write_only=True,validators=[validate_password])
    first_name=serializers.CharField(max_length=50,allow_blank=False,required=True)
    last_name=serializers.CharField(max_length=50,allow_blank=False,required=True)


    def create(self,validated_data):
       return CustomUser.objects.create_user(**validated_data)

    def validate_email(self,value):
        email=value.lower()
        already_registered=CustomUser.objects.filter(email__iexact=email).exists()

        if already_registered:
            raise serializers.ValidationError('A user with this email already exists.')

        return email


    trim_whitespace=False
    
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','last_name','password']

    