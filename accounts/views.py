from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from accounts.forms import MyUserCreationForm, UserUpdateForm
from accounts.models import User

from verify_email.email_handler import send_verification_email

# Create your views here.

@login_required(login_url='accounts-login')
def home(request):
    """
    User Home View

    This view redirects authenticated users to their profile page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirection to the user's profile page.

    """
    return redirect('accounts-profile', username=request.user.username)

def profile(request, username):
    """
    User Profile View

    This view displays a user's profile based on their username.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user to display.

    Returns:
        HttpResponse: The user's profile page or a 404 error if the user does not exist.

    """
    try:
        user = User.objects.get(username=username)
    except:
        return Http404("User does not exist")

    return render(request, 'accounts/profile.html', {
        'user': user
    })

@login_required(login_url='accounts-login')
def updateProfile(request):
    """
    User Profile Update View

    This view allows authenticated users to update their profile information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The user's profile update form.
        Redirect: A redirection to the user's profile page if the form is valid.

    """
    user = request.user
    form = UserUpdateForm(instance=user)

    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts-profile', username=user.username)
        
    return render(request, 'accounts/update_profile.html', {
        'form': form
    })

@login_required(login_url='accounts-login')
def deleteUser(request):
    """
    User Account Deletion View

    This view allows authenticated users to delete their account.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The user account deletion page.
        Redirect: A redirection to the accounts home page if the user is deleted.

    """
    user = request.user
    if request.method == "POST":
        try:
            password = request.POST.get('password')
            authenticated_user = authenticate(request, email=user.email, password=password)
            if authenticated_user is not None:
                logout(request)
                authenticated_user.delete()
                return redirect('accounts-home')
            else:
                messages.error(request, 'An error occured, you may have entered your password wrong.')
        except:
            messages.error(request, 'An error occured, you may have entered your password wrong.')
    
    return render(request, 'accounts/delete_user.html')

def registerUser(request):
    """
    User Registration View

    This view allows users to register by providing their registration details.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The user registration form or a success message on successful registration.
        Redirect: A redirection to the accounts home page if the form is valid.

    """
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = send_verification_email(request, form)
            except:
                return HttpResponse("An error occured, kindly contact the admin")
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            messages.success(request, 'Kindly verify your email using a link you just received.')
            return redirect('accounts-home')
    
    return render(request, 'accounts/register.html', {
        'form': form
    })

def loginUser(request):
    """
    User Login View

    This view allows users to log in using their email and password.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The login form or a redirection to the user's home page on successful login.

    """
    if request.user.is_authenticated == True:
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
    """
    User Logout View

    This view allows authenticated users to log out.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        Redirect: A redirection to the user's home page after logout.

    """
    logout(request)
    return redirect('accounts-home')