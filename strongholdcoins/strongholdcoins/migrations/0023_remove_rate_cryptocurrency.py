# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-03 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strongholdcoins', '0022_auto_20171003_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='cryptocurrency',
        ),
    ]
