# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 07:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160119_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='established',
            field=models.DateField(default=datetime.datetime(2016, 1, 21, 7, 26, 32, 8155)),
        ),
        migrations.AlterField(
            model_name='senior',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 21, 7, 26, 32, 7368)),
        ),
        migrations.AlterField(
            model_name='youth',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 21, 7, 26, 32, 8766)),
        ),
    ]
