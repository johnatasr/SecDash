from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from vulnerabilities.models import Vulnerability
from datetime import datetime


class VulneListCreateAPIViewTestCase(APITestCase):

    def setUp(self):
        self.username = "test"
        self.email = "testn@test.com"
        self.password = "Test123@"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        response = self.client.post('/users/token/obtain/', {'username': self.username, 'password': self.password},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.token = response.data['access']

        self.vulne = Vulnerability.objects.create(
            title='VULNE1',
            severity='HIGH',
            cvss=9,
            publication_date=datetime.now(),
            corrected=False
        )

        self.vulne = Vulnerability.objects.create(
            title='VULNE2',
            severity='MEDIUM',
            cvss=6,
            publication_date=datetime.now(),
            corrected=False
        )

    def test_filter_vulne(self):
        response = self.client.get('/api/vulnerabilities/filter_vulnerabilities/', {'page': 1, 'severity': 'HIGH'},
                                    HTTP_AUTHORIZATION='JWT ' + self.token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_correct_vulne(self):
        response = self.client.post('/api/vulnerabilities/correct_vulnerabilitie/',
                                    {"id": self.vulne.id},
                                    format='json',
                                    HTTP_AUTHORIZATION='JWT ' + self.token)
        self.assertEqual(200, response.status_code)

    def test_total_vulne(self):
        response = self.client.get('/api/vulnerabilities/get_total_vulnerabilities/',
                                    HTTP_AUTHORIZATION='JWT ' + self.token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['totalVulnerabilities'], 2)
        self.assertEqual(response.data['notCorrected'], 2)