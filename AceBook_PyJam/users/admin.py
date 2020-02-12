from django.contrib import admin
from .models import Posts, Friend

# Register your models here.

class UserPosts(admin.ModelAdmin):
    readonly_fields = ('post_created',)

admin.site.register(Posts, UserPosts)
admin.site.register(Friend)