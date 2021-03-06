# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 08:31
from __future__ import unicode_literals

import blog.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20160122_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='established',
            field=models.DateField(default=datetime.datetime(2016, 1, 27, 8, 31, 31, 592256)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='포스팅 제목을 100자 이내로 써주세요', max_length=100, validators=[blog.models.min_length_validator]),
        ),
        migrations.AlterField(
            model_name='senior',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 27, 8, 31, 31, 591489)),
        ),
        migrations.AlterField(
            model_name='youth',
            name='birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 27, 8, 31, 31, 592915)),
        ),
    ]
