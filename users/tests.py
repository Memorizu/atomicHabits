import json

from django.urls import reverse
from rest_framework import status

from habit.tests.base import BaseTestCase
from users.models import User


class UserTestCase(BaseTestCase):
    def setUp(self):

        self.user_data = {
            'username': 'test',
            'email': 'test@example.com',
            'password': 'test'
        }

    def test_create(self):
        user_create = reverse('user:user_create')
        response = self.client.post(user_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_token(self):
        user = User.objects.create(
            username='test',
            email='test@example.com',

        )
        user.set_password('test')
        user.save()
        user_token = reverse('user:token')
        token_response = self.client.post(user_token, data=self.user_data, format='json')

        self.assertEqual(token_response.status_code, status.HTTP_200_OK)

    def test_refresh_token(self):
        user = User.objects.create(
            username='test',
            email='test@example.com',

        )
        user.set_password('test')
        user.save()
        user_token = reverse('user:token')
        user_token = self.client.post(user_token, data={'username': user.username, 'email': user.email, 'password': 'test'})
        refresh = user_token.json().get('refresh')
        user_refresh_token = reverse('user:refresh_token')
        response = self.client.post(user_refresh_token, data=json.dumps({'refresh': refresh}), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
