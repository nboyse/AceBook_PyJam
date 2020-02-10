from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(req):
    return render(req, 'users/index.html')


def about(req):
    return render(req, 'users/about.html')


def register(req):
    return render(req, 'users/register.html')


def login(req):
    return render(req, 'users/login.html')
