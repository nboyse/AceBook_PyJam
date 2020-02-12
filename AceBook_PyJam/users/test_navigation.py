from django.test import TestCase
from django.urls import resolve
from .views import home
from .views import log_in
from django.contrib.auth.models import User
from django.test import Client
from django.db import models
from .models import Posts


# Create your tests here.

class TestNavigation(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_valid_user(self):
        u = User.objects.create(username='test3', password='Bar')
        data = {'username': u.username, 'password': u.password,}
        form = Posts
        self.assertTrue(form)
