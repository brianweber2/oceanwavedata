# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 16:04
from __future__ import unicode_literals

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20161007_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]