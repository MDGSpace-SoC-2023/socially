from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    username = None
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


     

    