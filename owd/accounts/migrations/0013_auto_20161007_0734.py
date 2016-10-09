# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20161007_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]