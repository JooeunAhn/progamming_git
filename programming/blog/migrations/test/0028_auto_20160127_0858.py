# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 08:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20160127_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='established',
            field=models.DateField(default=datetime.datetime(2016, 1, 27, 8, 58, 53, 956791)),
        ),
        migrations.AlterField(
            model_name='senior',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 27, 8, 58, 53, 956047)),
        ),
        migrations.AlterField(
            model_name='youth',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 27, 8, 58, 53, 957389)),
        ),
    ]
