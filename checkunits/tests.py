"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import WelcomeView, AboutUsView

class UrlTests(TestCase):
    def test_welcome_url(self):
        welcome = resolve(reverse('checkunits:welcome'))
        return self.assertEqual(welcome.func.__name__,
                                WelcomeView.__name__)



class test_aboutus_url(TestCase):
    def test_welcome_url(self):
        aboutus = resolve(reverse('checkunits:aboutus'))
        return self.assertEqual(aboutus.func.__name__,
                                AboutUsView.__name__)