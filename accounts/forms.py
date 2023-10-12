from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username', 'bio']

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'bio']