from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class UserApiAuthTestCase(APITestCase):

    def setUp(self):
        self.username = "test"
        self.email = "testn@test.com"
        self.password = "Test123@"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = ''

    def test_api_jwt(self):
        self.user.is_active = False
        self.user.save()

        response = self.client.post('/users/token/obtain/', {'username': self.username, 'password': self.password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.user.is_active = True
        self.user.save()

        response = self.client.post('/users/token/obtain/', {'username': self.username, 'password': self.password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)