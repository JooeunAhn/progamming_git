# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 09:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160114_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='established',
            field=models.DateField(default=datetime.datetime(2016, 1, 15, 9, 7, 28, 978589)),
        ),
        migrations.AddField(
            model_name='senior',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 15, 9, 7, 28, 977939)),
        ),
        migrations.AddField(
            model_name='youth',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 15, 9, 7, 28, 979246)),
        ),
    ]