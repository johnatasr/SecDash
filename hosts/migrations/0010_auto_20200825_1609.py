# Generated by Django 3.1 on 2020-08-25 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0009_auto_20200825_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='vulnerability',
            new_name='vulnerabilities',
        ),
        migrations.AlterField(
            model_name='hostsfiles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 16, 9, 48, 586802), verbose_name='Emission Date'),
        ),
    ]
