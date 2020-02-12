from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Posts(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=10000)
    post_like = models.BooleanField(null=True)   # Change this to a counter
    post_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title


class PostsReplies(models.Model):
    reply_content = models.CharField(max_length=10000)
    reply_created = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    image = models.FileField(upload_to='images/')
    url = models.URLField(blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
