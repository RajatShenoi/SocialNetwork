from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.manager import UserManager

# Create your models here.
class User(AbstractUser):
    """
    Custom User Model

    This class defines a custom User model that extends the built-in `AbstractUser` model provided by Django.
    It includes additional fields and configurations for user management.

    Attributes:
        email (EmailField): The user's email address (unique and required).
        bio (TextField): A user's biography (optional).
        avatar (ImageField): An image field for the user's avatar (with a default image).
        USERNAME_FIELD (str): The field used for authentication (set to 'email').
        REQUIRED_FIELDS (list): A list of required fields for user creation (contains 'username').

    Methods:
        __str__(): A method to provide a string representation of the user. "<email> (<username>)"

    """
    email = models.EmailField(unique=True, null=False, blank=False)
    bio = models.TextField(max_length=500, blank=True, null=True)
    avatar = models.ImageField(upload_to="images/avatars", null=False, blank=False, default="images/avatars/default.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.username})"