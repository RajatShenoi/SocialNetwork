from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from accounts.forms import MyUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def registerUser(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('accounts-home')

    return render(request, 'accounts/register.html', {
        'form': form
    })

def logoutUser(request):
    logout(request)
    return redirect('accounts-home')