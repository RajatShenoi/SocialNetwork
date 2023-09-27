from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.manager import UserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    bio = models.TextField(max_length=500, blank=True, null=True)
    avatar = models.ImageField(upload_to="images/avatars", null=False, blank=False, default="images/avatars/default.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.username})"