"""AceBook_PyJam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile_pk'),
    path('updateprofile', views.update_profile, name='updateprofile'),
    path('delete', views.deletepost, name='deletepost'),
    path('postreply', views.postreply, name='postreply'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.manage_friends,
        name='manage_friends'),

    # Auth Routes   
    path('signup/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'),

    # Admin
    path('admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
