# Generated by Django 3.1 on 2020-08-28 05:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0010_auto_20200825_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostsfiles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 28, 2, 28, 30, 185617), verbose_name='Emission Date'),
        ),
    ]
