from hosts.models import Host
from vulnerabilities.models import Vulnerability
from datetime import datetime
from django.test import TestCase


class HostsTest(TestCase):

    def setUp(self):
        Host.objects.create(
            hostname='HOSTNAME1',
            ip_adress='192.168.0.1',
        )
        Host.objects.create(
            hostname='HOSTNAME2',
            ip_adress='192.168.0.2',
        )


    def test_get_ip_adress(self):
        host_1 = Host.objects.get(hostname='HOSTNAME1')
        host_2 = Host.objects.get(hostname='HOSTNAME2')
        self.assertEqual(
            host_1.ip_adress, '192.168.0.1')
        self.assertEqual(
            host_2.ip_adress, '192.168.0.2')

    def test_insert_vulnerabilities(self):
        host_1 = Host.objects.get(hostname='HOSTNAME1')
        host_2 = Host.objects.get(hostname='HOSTNAME2')

        vulne_1 = Vulnerability.objects.create(
            title='VULNE1',
            severity='LOW',
            cvss=3,
            publication_date=datetime.now(),
            corrected=False
        )

        vulne_2 = Vulnerability.objects.create(
            title='VULNE2',
            severity='HIGH',
            cvss=9,
            publication_date=datetime.now(),
            corrected=False
        )

        host_1.vulnerabilities.add(vulne_1)
        host_1.save()

        host_2.vulnerabilities.add(vulne_2)
        host_2.save()

        self.assertEqual(
            vulne_1.id, Host.objects.filter(id=host_1.id).values('vulnerabilities')[0]['vulnerabilities'])
        self.assertEqual(
            vulne_2.id, Host.objects.filter(id=host_2.id).values('vulnerabilities')[0]['vulnerabilities'])
