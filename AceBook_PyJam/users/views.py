from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostsForm
from .models import Posts, Friend


def home(req):  # route landing page, home for non users
    if req.method == 'GET':
        posts = Posts.objects.order_by('-post_created')
        users = User.objects.exclude(id=req.user.id)
        friend = Friend.objects.filter(current_user=req.user.id)[0]
        friends = friend.users.all()

        print(friends)
        return render(req, 'users/index.html', {'form': PostsForm(), 'posts': posts, 'user': req.user, 'users': users, 'friends': friends})
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
def profile(req, pk=None):
    if pk:
        f_user = User.objects.get(pk=pk)
    else:
        f_user = req.user
    myposts = Posts.objects.filter(user=f_user).order_by('-post_created')
    return render(req, 'users/profile.html', {'myposts': myposts, 'f_user': f_user})


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


def manage_friends(req, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.add_friend(req.user, friend)
    elif operation == 'remove':
        Friend.remove_friend(req.user, friend)
    return redirect('home')
