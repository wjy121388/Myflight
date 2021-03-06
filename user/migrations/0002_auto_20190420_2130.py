# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-20 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytrip',
            name='datetime',
            field=models.DateTimeField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='username@email.com', max_length=254),
        ),
    ]
