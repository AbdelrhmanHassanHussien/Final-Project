from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book

class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        # Create a user with known credentials
        self.username = 'user001'
        self.password = '1234qazW'
        self.password2 = '12345asdf'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client = Client()
        
    def test_login_with_correct_credentials(self):
        # Attempt to log in with correct credentials
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login, "Login should succeed with correct credentials.")
        
    def test_login_with_incorrect_credentials(self):
        # Attempt to log in with incorrect credentials
        login = self.client.login(username=self.username, password=self.password2)
        # login = self.client.login(username=self.username, password='4545456465')

        self.assertFalse(login, "Login should fail with incorrect password.")
        
        # Check if the user is redirected (302 status code)
        response = self.client.get(reverse('homeclinic'))  # Adjust this URL to a relevant one for your app
        self.assertEqual(response.status_code, 302)  # Expecting redirection
        
        # Follow the redirect
        redirect_url = response.url
        response = self.client.get(redirect_url)
        self.assertEqual(response.status_code, 200)  # Should be able to access the login page or error page
        
        # Optionally, check if an error message or login form is present
        self.assertContains(response, "Login")  # Adjust this as needed to match your application's login page content


