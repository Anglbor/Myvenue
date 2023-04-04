from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            messages.success(request, "You are logged in")
            return redirect('home')
        else:
            messages.success(request, 'There was wrong login, Try again')
            # Return an 'invalid login' error message
            return redirect('login_user')

    else:
        return render(request, 'auth/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Register was successful")
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, "auth/register_user.html", {"form": form})
