# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-09 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strongholdcoins', '0033_auto_20171009_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bank',
            field=models.CharField(blank=True, choices=[('GT Bank', 'GT BANK'), ('Zenith Bank', 'ZENITH BANK'), ('Stanbic Bank', 'STANBIC BANK'), ('EcoBank', 'ECOBANK'), ('UniBank', 'UNIBANK'), ('Cal Bank', 'CAL BANK')], max_length=50, null=True),
        ),
    ]