from django.db import models

# Create your models here.


class User(models.Model):
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
    gender = models.CharField(max_length=15)
    dob = models.DateField

