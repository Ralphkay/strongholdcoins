# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-13 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strongholdcoins', '0005_auto_20170913_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='other_names',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
