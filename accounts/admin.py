from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserAdminForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"))
    class Meta:
        model = User
        fields = '__all__'


class CustomUserAdmin(UserAdmin):
    form = CustomUserAdminForm
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'username', 'email', 'password')}),
        ('Additional Info', {'fields': ('bio', 'avatar')}),
        ('Permissions', {'fields': ('groups', 'user_permissions', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')}),
    )

admin.site.register(User, CustomUserAdmin)