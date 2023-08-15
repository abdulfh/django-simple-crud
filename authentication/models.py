from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.db import models
from django.utils import timezone
from authentication.managers import CustomUserManager




class Admin(AbstractBaseUser):
    email = models.EmailField(("Email Address"), unique=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class User(Admin):
    username = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    zip = models.IntegerField()
    message = models.TextField()
    address = models.TextField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email