# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 02:31
from __future__ import unicode_literals

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import programming.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(default='hanyang@sap.com', max_length=254)),
                ('url', models.URLField(default='http://localhost')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='포스팅 제목을 100자 이내로 써주세요', max_length=100, validators=[blog.models.min_length_validator])),
                ('content', models.TextField()),
                ('phone', blog.models.PhoneField(blank=True, max_length=10)),
                ('photo', models.ImageField(blank=True, upload_to=programming.utils.random_name_upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Senior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('email', models.EmailField(default='hanyang@sap.com', max_length=254)),
                ('career', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Youth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('email', models.EmailField(default='seoul@sap.com', max_length=254)),
                ('career', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
