from django.db import models

# Create your models here.
class Vulnerability(models.Model):
    title = models.CharField('Title', max_length=588, null=True, blank=True)
    severity = models.CharField('Severity', max_length=588, null=True, blank=True)
    cvss = models.DecimalField('CVSS', decimal_places=2, max_digits=10, null=True, blank=True)
    publication_date = models.DateTimeField('Publication Date', null=True, blank=True)
    corrected = models.BooleanField('Corrected ?', null=True, blank=True)

    class Meta:
        verbose_name = "vulnerabilities"
        verbose_name_plural = "1. Vulnerabilities"

    def __str__(self):
        return f'ID: {self.id} | Title: {self.title}'