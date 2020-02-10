from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=10000)
    post_like = models.BooleanField(blank=True)
    post_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title