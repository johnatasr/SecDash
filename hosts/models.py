from django.db import models
from vulnerabilities.models import Vulnerability
from datetime import datetime
# Create your models here.


class Host(models.Model):
    hostname = models.CharField('Hostname', max_length=588, null=True, blank=True)
    ip_adress = models.CharField('Ip Adress', max_length=588, null=True, blank=True)
    vulnerabilities = models.ManyToManyField(Vulnerability,  blank=True)


    class Meta:
        verbose_name = "hosts"
        verbose_name_plural = "1. Hosts"

    def __str__(self):
        return str(self.id)


class HostsFiles(models.Model):
    STATUS = (
        ('F', 'Finished'),
        ('R', 'Running'),
        ('E', 'Error')
    )

    key = models.CharField(u"Key", max_length=30, unique=True, null=False)
    file = models.FileField(
        "File", max_length=512, upload_to='files')
    date = models.DateTimeField(u"Emission Date", default=datetime.now())
    status = models.CharField(u"Process Status", max_length=1, choices=STATUS,
                              null=False, help_text=u'Finished/Running/Error', default='F')
    exception = models.TextField(
        u"Exceptions", max_length=512, null=True, blank=True)
    exceptions_file = models.FileField(
        u"Exceptions File", max_length=512, upload_to='files', null=True)

    class Meta:
        verbose_name = "hosts files"
        verbose_name_plural = "2. Hosts Files"

    def __str__(self):
        return str(self.id)
