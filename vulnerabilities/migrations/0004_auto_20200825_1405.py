# Generated by Django 3.1 on 2020-08-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0003_auto_20200825_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerability',
            name='cvss',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=4, null=True, verbose_name='CVSS'),
        ),
    ]
