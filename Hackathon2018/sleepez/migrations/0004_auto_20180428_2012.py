# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-29 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleepez', '0003_auto_20180428_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='Latitude',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shelter',
            name='longitude',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]
