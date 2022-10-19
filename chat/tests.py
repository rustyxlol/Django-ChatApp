from django.test import TestCase
from django.test import Client
from chat.urls import urlpatterns, path
from django.test import TestCase
from django.test import Client

class TestViews(TestCase):

    def test_url_login_redirect_not_logged_in(self):
        with self.settings(DEBUG=False):
            response = self.client.get('/')
            print('Test url redirect to login page')
            self.assertEqual(response.status_code, 302 )
            self.assertEqual(response['location'], '/login/?next=/')
            
    def test_home_page_visitor(self):
        with self.settings(DEBUG=False):
            response = self.client.get('/login/?next=/')
            print('Test homepage guest')
            self.assertContains(response, 'Log In')
            self.assertContains(response, 'Username')
            self.assertContains(response, 'Password')
            self.assertContains(response, 'Need An Account?')
            self.assertContains(response, 'Sign Up Now')

    def test_register_page(self):
        with self.settings(DEBUG=False):
            response = self.client.get('/register/')
            print('Test register page')
            self.assertContains(response, 'Join Today')
            self.assertContains(response, 'Username')
            self.assertContains(response, 'Password')
            self.assertContains(response, 'Password confirmation')
            self.assertContains(response, 'Already Have An Account?')
            self.assertContains(response, 'Sign In')

    #TODO: Test logged in homepage(chat_home), Test logged out homepage(base.html),(chat_room, Profile(models), public_rooms, 
    # ChatConsumer, and more. 

