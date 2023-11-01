from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    """
    Custom User Creation Form

    This form is used to create a new user. It is based on the default
    UserCreationForm, but it adds the email and bio fields.

    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username', 'bio']

class UserUpdateForm(ModelForm):
    """
    Custom User Update Form

    This form is used to update a user. It is based on the default
    ModelForm, but it adds the avatar, first_name, last_name and bio fields.

    """
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'bio']