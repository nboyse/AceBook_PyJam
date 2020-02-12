from django.contrib import admin
from .models import Posts, Profile

# Register your models here.


class UserProfile(admin.ModelAdmin):
    class Meta:
        model = Profile
        field = ('bio', 'location')


class UserPosts(admin.ModelAdmin):
    readonly_fields = ('post_created',)


admin.site.register(Profile, UserProfile)
admin.site.register(Posts, UserPosts)