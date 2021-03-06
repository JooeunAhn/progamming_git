# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 07:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterpise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('established', models.DateField(default=datetime.datetime)),
                ('email', models.EmailField(default='hanyang@sap.com', max_length=254)),
                ('url', models.URLField(default='http://localhost')),
            ],
        ),
        migrations.CreateModel(
            name='Senior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('birth', models.DateField(default=datetime.datetime)),
                ('email', models.EmailField(default='hanyang@sap.com', max_length=254)),
                ('career', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Youth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('birth', models.DateField(default=datetime.datetime)),
                ('email', models.EmailField(default='seoul@sap.com', max_length=254)),
                ('career', models.TextField()),
            ],
        ),
    ]
