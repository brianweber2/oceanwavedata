# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20161005_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='display_name',
        ),
    ]
