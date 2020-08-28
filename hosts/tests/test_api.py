from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from hosts.models import Host
from vulnerabilities.models import Vulnerability
from datetime import datetime


class IncidentsListCreateAPIViewTestCase(APITestCase):

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

        self.host = Host.objects.create(
            hostname='HOSTNAME1',
            ip_adress='192.168.0.1',
        )

        self.vulne = Vulnerability.objects.create(
            title='VULNE1',
            severity='HIGH',
            cvss=9,
            publication_date=datetime.now(),
            corrected=False
        )

    def test_list_hosts(self):

        response = self.client.get('/api/hosts/list_hosts/', {'page': 1}, HTTP_AUTHORIZATION='JWT ' + self.token)
        self.assertEqual(200, response.status_code)
        hosts = Host.objects.all().count()
        self.assertEqual(hosts, len(response.data))

    def test_filter_host(self):
        data = {
            'hostname': 'HOSTNAME3',
            'ip_adress': '192.168.0.3',
        }
        host = Host.objects.create(**data)
        host.vulnerabilities.add(self.vulne)
        host.save()

        response = self.client.get('/api/hosts/filter_hosts/', {'page': 1, 'vulnerabilityTitle': 'VULNE1'},
                                   format='json', HTTP_AUTHORIZATION='JWT ' + self.token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_detail_host(self):
        response = self.client.get('/api/hosts/detail_host/',
                                    {"id": self.host.id},
                                    format='json',
                                    HTTP_AUTHORIZATION='JWT ' + self.token)
        self.assertEqual(200, response.status_code)

