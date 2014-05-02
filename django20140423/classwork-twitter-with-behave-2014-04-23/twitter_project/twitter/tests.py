"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class SimpleTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login_page(self):
        self.assertEquals(reverse("twitter:login"), '/twitter/login/')
        response = self.client.get(reverse("twitter:login"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Re")

        response = self.client.get(reverse("twitter:home"))
        self.assertEquals(response.status_code, 302)

        #self.client.post(URL, {'username':username})

        user = User.objects.create_user(
        	username='user',
        	password='user'
        	)
        login_status = self.client.login(username='user',
        	password='user')
        self.assertTrue(login_status)

		response = self.client.get(reverse("twitter:home"))
        self.assertEquals(response.status_code, 200)