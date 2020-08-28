# Generated by Django 3.1 on 2020-08-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0002_auto_20200825_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vulnerability',
            options={'verbose_name': 'vulnerabilities', 'verbose_name_plural': '1. Vulnerabilities'},
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='cvss',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True, verbose_name='CVSS'),
        ),
    ]