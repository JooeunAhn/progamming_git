# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 01:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160116_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='established',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 1, 31, 29, 86749)),
        ),
        migrations.AlterField(
            model_name='senior',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 1, 31, 29, 86051)),
        ),
        migrations.AlterField(
            model_name='youth',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 1, 31, 29, 87434)),
        ),
    ]
