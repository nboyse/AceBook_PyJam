from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(req): # route landing page, home for non users
    return render(req, 'users/index.html')


def about(req):
    return render(req, 'users/about.html')


def register(req):
    if req.method == 'GET':
        return render(req, 'users/temp_register.html', {
            'form': UserCreationForm()
        })
    elif req.method == 'POST':
        if req.POST['password1'] == req.POST['password2']:
            try:
                user = User.objects.create_user(req.POST['username'], password=req.POST['password1'])
                user.save()
                login(req, user)
                return redirect('home')
            except IntegrityError:
                return render(req, 'users/temp_register.html', {'form': UserCreationForm(),
                    'error': "Username has already been taken, please pick another one"
            })

        else:
            # Send password error (didnt match)
            return render(req, 'users/temp_register', {
                'form': UserCreationForm(),
                'error': "Passwords did not match, please check and try again"
        })


def log_in(req):
    if req.method == 'GET':
        return render(req, 'users/login.html', {
            'form': AuthenticationForm()
        })
    elif req.method == 'POST':
        user = authenticate(req, username=req.POST['username'], password=req.POST['password'])
        if user is None:
            return render(req, 'users/login.html', {
                'form': AuthenticationForm(),
                'error': 'Invaid Username/password please try again'
            })
        else:
            login(req, user)
            return redirect('user-feed')


def log_out(req):
    if req.method == 'POST':
        logout(req)
        return redirect('home')


def user_feed(req):
    return render(req, 'users/user_feed.html')
