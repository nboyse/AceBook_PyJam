from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostsForm, ReplyForm, ProfileForm, UserForm
from .models import Posts, PostsReplies, Friend


# Note for readers of the code in the future, users refers to the currently logged in user with the exception of friends, on the profile page, 
# f_user refers to the current user and users is swapped to work in the friends list 🤷


def handle_uploaded_file(f):
    # with open(f, 'wb+') as destination:
    for chunk in f.chunks():
        f.write(chunk)


def home(req):  # route landing page, home for non users
    if req.method == 'GET':
        posts = Posts.objects.order_by('-post_created')
        users = User.objects.exclude(id=req.user.id)
    
        return render(req, 'users/index.html', {'form': PostsForm(), 'posts': posts, 'user': req.user, 'users': users})
    else:
        try:
            form = PostsForm(req.POST)
            newpost = form.save(commit=False)
            newpost.user = req.user
            newpost.save()
            return redirect('home')
        except ValueError:
            return render(req, 'users/index.html', {'form': PostsForm(), 'error': 'Bad data passed in. Try again.'})


def postreply(req):
    return render(req, 'users/postreply.html')


def about(req):
    return render(req, 'users/about.html')


def register(req):
    if req.method == 'GET':
        return render(req, 'users/register.html', {
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
                return render(req, 'users/register.html', {'form': UserCreationForm(),
                                                                'error': "Username has already been taken, please "
                                                                         "pick another one "
                                                           })

        else:
            # Send password error (didnt match)
            return render(req, 'users/register.html', {
                'form': UserCreationForm(),
                'error': "Passwords did not match, please check and try again"
            })


@login_required
def profile(req, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = req.user

    users = User.objects.exclude(id=req.user.id)
    myposts = Posts.objects.filter(user=user).order_by('-post_created')

    if (Friend.objects.filter(current_user=req.user.id)):
        friend = Friend.objects.filter(current_user=req.user.id)[0]
        friends = friend.users.all()
        return render(req, 'users/profile.html', {'myposts': myposts, 'users': users, 'user': user, 'friends': friends})
    else:
        friends = ""
        return render(req, 'users/profile.html', {'myposts': myposts, 'user': user, 'friends': friends, 'users': users})


@login_required
# @transaction.atomic
def update_profile(req):
    if req.method == 'POST':
        user_form = UserForm(req.POST, instance=req.user, )
        profile_form = ProfileForm(req.POST, req.FILES, instance=req.user.profile,)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            handle_uploaded_file(req.FILES['image'])
            return redirect('profile')
        else:
            pass
    else:
        user_form = UserForm(instance=req.user)
        profile_form = ProfileForm(instance=req.user.profile)
    return render(req, 'users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def deletepost(req, pk):
    if req.method == 'POST':
        post_id = (int(req.POST.get('item_id')))
        post = Posts.objects.get(id=post_id)
        post.delete()
        return redirect('home')
        # profile = User.objects.get(id=pk)


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