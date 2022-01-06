from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        return self.create_user(email, name, password, **kwargs)

class User(AbstractUser):
    name = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    username = None

    REQUIRED_FIELDS = ['name']
    objects = UserManager()
    USERNAME_FIELD = 'email'