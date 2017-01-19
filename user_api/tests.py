from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CreateUserTest(APITestCase):
    def setUp(self):
        self.create_data = {'email': 'test@test.com', 'password1': 'test1234', 'password2': 'test1234'}
        self.login_data = {'email': 'test@test.com', 'password': 'test1234'}

    def test_can_create_user(self):
        response = self.client.post('/api/registration/', self.create_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
