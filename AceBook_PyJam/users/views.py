from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostsForm
from .models import Posts


def home(req):  # route landing page, home for non users
    if req.method == 'GET':
        posts = Posts.objects.order_by('-post_created')
        print(posts)
        return render(req, 'users/index.html', {'form': PostsForm(), 'posts': posts, 'user': req.user})
    else:
        try:
            form = PostsForm(req.POST)
            newpost = form.save(commit=False)
            newpost.user = req.user
            newpost.save()
            return redirect('home')
        except ValueError:
            return render(req, 'users/index.html', {'form': PostsForm(), 'error': 'Bad data passed in. Try again.'})


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
                user = User.objects.create_user(req.POST['username'],
                                                password=req.POST['password1'],
                                                email=req.POST['email'],
                                                first_name=req.POST['first_name'],
                                                last_name=req.POST['last_name'])
                user.save()
                login(req, user)
                return redirect('home')
            except IntegrityError:
                return render(req, 'users/temp_register.html', {'form': UserCreationForm(),
                                                                'error': "Username has already been taken, please "
                                                                         "pick another one "
                                                                })

        else:
            # Send password error (didnt match)
            return render(req, 'users/temp_register.html', {
                'form': UserCreationForm(),
                'error': "Passwords did not match, please check and try again"
            })


@login_required
def profile(req):
    myposts = Posts.objects.filter(user=req.user).order_by('-post_created')
    return render(req, 'users/profile.html', {'myposts': myposts})


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
                'error': 'Invalid Username/password please try again'
            })
        else:
            login(req, user)
            return redirect('profile')


def log_out(req):
    if req.method == 'POST':
        logout(req)
        return redirect('home')

#
# def user_feed(req):
#     return render(req, 'users/user_feed.html')
