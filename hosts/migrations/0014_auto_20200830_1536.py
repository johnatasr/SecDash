# Generated by Django 3.1 on 2020-08-30 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0013_auto_20200830_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostsfiles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 30, 15, 36, 50, 770346), verbose_name='Emission Date'),
        ),
    ]