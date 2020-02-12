from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=10000)
    post_like = models.BooleanField(null=True)
    post_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User,
                                     related_name='owner',
                                     null=True,
                                     on_delete=models.CASCADE)

    @classmethod
    def add_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
