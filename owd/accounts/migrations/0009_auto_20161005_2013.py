# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='display_name',
            field=models.CharField(max_length=140),
        ),
    ]
