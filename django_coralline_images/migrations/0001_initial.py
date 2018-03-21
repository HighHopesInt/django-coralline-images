# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField(verbose_name='User ID')),
                ('image_id', models.CharField(max_length=71, verbose_name='Docker image ID')),
                ('created', models.DateTimeField(verbose_name='Created')),
                ('size', models.PositiveIntegerField(verbose_name='Size')),
            ],
        ),
    ]
