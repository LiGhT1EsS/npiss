# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_pissuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pissactivecode',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pissactivecode',
            name='user_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
