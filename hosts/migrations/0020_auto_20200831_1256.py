# Generated by Django 3.1 on 2020-08-31 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0019_auto_20200831_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostsfiles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 31, 12, 56, 41, 618894), verbose_name='Emission Date'),
        ),
    ]
