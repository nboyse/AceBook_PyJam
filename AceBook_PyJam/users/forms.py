from django.forms import ModelForm
from .models import Posts, PostsReplies, Profile
from django.contrib.auth.models import User
from django import forms


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['post_title', 'post_content']


class ReplyForm(ModelForm):
    class Meta:
        model = PostsReplies
        fields = ['reply_content']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'image', 'url')
        file = forms.FileField()
