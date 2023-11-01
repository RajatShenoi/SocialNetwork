from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)

from . import views

urlpatterns = [
    # paths related to user profile
    path('', views.home, name='accounts-home'),
    path('profile/<str:username>/', views.profile, name='accounts-profile'),
    path('update/', views.updateProfile, name='accounts-update'),

    # paths related to user authentication
    path('login/', views.loginUser, name='accounts-login'),
    path('register/', views.registerUser, name='accounts-register'),
    path('logout/', views.logoutUser, name='accounts-logout'),

    # paths related to password reset functionality
    path('password-reset/', PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),

    # paths related to user deletion
    path('delete/', views.deleteUser, name='accounts-delete'),
]