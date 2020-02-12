from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.manage_friends,
        name='manage_friends')
]