from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.log_in, name='login'),
    path('user-feed', views.user_feed, name='user-feed')

]