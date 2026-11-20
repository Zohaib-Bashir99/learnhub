import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email=models.EmailField(unique=True)
    username=None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=['first_name','last_name']

    object=CustomUserManager()