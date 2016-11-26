# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PissActiveCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_created=True, default=None)),
                ('user_id', models.BigIntegerField()),
                ('active_code', models.CharField(max_length=64, unique=True)),
                ('used', models.BooleanField(default=False)),
                ('used_time', models.DateTimeField(default=None)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'piss_active_code',
            },
        ),
        migrations.CreateModel(
            name='PissUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_created=True, default=None)),
                ('username', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=512)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'piss_users',
            },
        ),
        migrations.CreateModel(
            name='PissUserExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_created=True, default=None)),
                ('user_id', models.BigIntegerField()),
                ('access_key', models.CharField(blank=True, max_length=40)),
                ('secret_key', models.CharField(blank=True, max_length=40)),
                ('domain', models.CharField(max_length=255)),
                ('use_qiniu', models.BooleanField(default=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'piss_user_extra',
            },
        ),
    ]