from django.test import TestCase
from django.urls import resolve
from .views import home
from .views import log_in
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.

class TestNavigation(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
