# Generated by Django 3.1 on 2020-08-30 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0014_auto_20200830_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostsfiles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 30, 18, 52, 29, 879079), verbose_name='Emission Date'),
        ),
    ]