from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(req):
    return render(req, 'users/index.html')

