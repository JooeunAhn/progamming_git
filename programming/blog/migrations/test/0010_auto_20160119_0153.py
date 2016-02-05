# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 01:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160119_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='established',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 1, 53, 53, 71303)),
        ),
        migrations.AlterField(
            model_name='senior',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 1, 53, 53, 70641)),
        ),
        migrations.AlterField(
            model_name='youth',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 1, 53, 53, 71969)),
        ),
    ]
