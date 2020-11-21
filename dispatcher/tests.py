
from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.template.loader import render_to_string


class AuthenticationTestCases(TestCase):

    def test_register(self):
        request_body = {
            'email': 'valid@email.address',
            'password': 'secure_password'
        }
        response = self.client.post(reverse('dispatcher:register'), request_body)
        print(response.data)
        self.assertEqual(200, response.status_code)
        self.assertIn('Continue registeration from the email sent to you.', str(response.data))
