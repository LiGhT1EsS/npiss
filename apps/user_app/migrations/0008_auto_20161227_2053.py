# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-27 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_auto_20161227_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pissuser',
            name='last_login_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
