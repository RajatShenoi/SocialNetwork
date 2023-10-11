from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from accounts.forms import MyUserCreationForm
from accounts.models import User

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

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('accounts-home')
    
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
            return render(request, 'accounts/login.html')
        
        user = authenticate(request, email=user.email, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts-home')
        else:
            messages.error(request, 'Email or password is incorrect')
    
    return render(request, 'accounts/login.html')
        

def logoutUser(request):
    logout(request)
    return redirect('accounts-home')