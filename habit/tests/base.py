from django.urls import reverse
from rest_framework.test import APITestCase

from users.models import User


class BaseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='test',
            email='testuser',
            is_active=True
        )
        self.user.set_password('test')
        self.user.save()
        get_token = reverse('user:token')
        token_response = self.client.post(path=get_token, data={'email': 'testuser', 'password': 'test'})
        token = token_response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
