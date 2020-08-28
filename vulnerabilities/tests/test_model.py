from hosts.models import Host
from vulnerabilities.models import Vulnerability
from datetime import datetime
from django.test import TestCase


class VulneTest(TestCase):

    def setUp(self):
        Vulnerability.objects.create(
            title='VULNE1',
            severity='LOW',
            cvss=3,
            publication_date=datetime.now(),
            corrected=False
        )
        Vulnerability.objects.create(
            title='VULNE2',
            severity='HIGH',
            cvss=9,
            publication_date=datetime.now(),
            corrected=False
        )


    def test_get_title(self):
        vulne_1 = Vulnerability.objects.get(title='VULNE1')
        vulne_2 = Vulnerability.objects.get(title='VULNE2')
        self.assertEqual(
            vulne_1.title, 'VULNE1')
        self.assertEqual(
            vulne_2.title, 'VULNE2')

    def test_get_cvss(self):
        vulne_1 = Vulnerability.objects.get(title='VULNE1')
        vulne_2 = Vulnerability.objects.get(title='VULNE2')
        self.assertEqual(
            vulne_1.cvss, 3)
        self.assertEqual(
            vulne_2.cvss, 9)


