# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-09 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strongholdcoins', '0035_auto_20171009_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='crypto_currency',
            field=models.CharField(blank=True, choices=[('BITCOIN', 'BITCOIN'), ('ETHERIUM', 'ETHERIUM'), ('LITECOIN', 'LITECOIN')], max_length=12),
        ),
    ]
