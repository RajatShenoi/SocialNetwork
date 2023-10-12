from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accounts-home'),
    path('profile/<str:username>/', views.profile, name='accounts-profile'),
    path('update/', views.updateProfile, name='accounts-update'),

    path('login/', views.loginUser, name='accounts-login'),
    path('register/', views.registerUser, name='accounts-register'),
    path('logout/', views.logoutUser, name='accounts-logout')
]