# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-23 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_coralline_images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimage',
            name='tag',
            field=models.CharField(default='', max_length=500, verbose_name='Image tag'),
        ),
    ]