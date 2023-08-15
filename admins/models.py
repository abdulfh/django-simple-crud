from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AdminManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        return self.create_user(email, password, **extra_fields)


class Admin(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    
    objects = AdminManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.name