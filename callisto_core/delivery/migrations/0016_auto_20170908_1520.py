# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0015_auto_20170905_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='contact_voicemail',
            field=models.TextField(default=True),
        ),
    ]
