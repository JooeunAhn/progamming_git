# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 03:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160119_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='established',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 3, 8, 8, 843332)),
        ),
        migrations.AlterField(
            model_name='senior',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 3, 8, 8, 842669)),
        ),
        migrations.AlterField(
            model_name='youth',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 3, 8, 8, 844116)),
        ),
    ]
