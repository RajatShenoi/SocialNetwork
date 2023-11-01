from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserAdminForm(forms.ModelForm):
    """
    Custom User Admin Form

    This form extends the standard ModelForm for the User model and replaces the password field with
    a read-only password hash field in the admin panel.

    Attributes:
        password (ReadOnlyPasswordHashField): A read-only field for displaying the user's password hash.

    Meta:
        model (User): The User model associated with this form.
        fields (str): Specifies all fields to be included in the form.

    """
    password = ReadOnlyPasswordHashField(label=("Password"))
    class Meta:
        model = User
        fields = '__all__'


class CustomUserAdmin(UserAdmin):
    """
    Custom User Admin Configuration

    This class extends the UserAdmin class provided by Django and customizes the admin interface
    for the User model. It defines fieldsets to organize the user's information efficiently.

    Attributes:
        form (CustomUserAdminForm): The form to be used for user administration.
        fieldsets (tuple): Specifies the organization of fields in the admin panel.

    """
    form = CustomUserAdminForm
    fieldsets = (
        (
            None, {
                'fields': (
                    'first_name', 
                    'last_name', 
                    'username', 
                    'email', 
                    'password'
                )
            }
        ),
        (
            'Additional Info', {
                'fields': (
                    'bio', 
                    'avatar'
                )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'groups', 
                    'user_permissions', 
                    'is_active', 
                    'is_staff', 
                    'is_superuser', 
                    'last_login', 
                    'date_joined'
                )
            }
        ),
    )

admin.site.register(User, CustomUserAdmin)