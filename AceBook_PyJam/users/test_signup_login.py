from django.test import TestCase
from django.urls import resolve
from .views import log_in
from django.contrib.auth.models import User
from django.test import Client
from django.db import models
from django.db import IntegrityError


# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_register(self):
        user = User.objects.create(username='testuser1')
        user.set_password('test')
        user.save()


    def test_user_login(self):
        c = Client()
        logged_in = c.post('/login/', {'username': 'testusername', 'password': 'test'})
        logged_in.status_code
        response = c.get('/profile/')
        response.content


    def test_user_exists(self):
        user = User.objects.create(username='testusername')
        user.set_password('test')
        user.save()
