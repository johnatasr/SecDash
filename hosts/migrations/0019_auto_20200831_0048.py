# Generated by Django 3.1 on 2020-08-31 00:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0018_auto_20200830_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostsfiles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 31, 0, 48, 38, 956962), verbose_name='Emission Date'),
        ),
    ]
