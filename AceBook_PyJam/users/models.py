from django.db import models
from django import forms

# Create your models here.


class User(models.Model):
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
    dob = models.DateField
    gender = models.CharField(max_length=15)


