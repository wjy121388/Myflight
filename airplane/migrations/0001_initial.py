# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-14 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.CharField(max_length=100)),
                ('mileage', models.IntegerField()),
                ('aircraft_models', models.CharField(max_length=30)),
                ('flight_status', models.CharField(choices=[('1', '计划'), ('2', '起飞'), ('3', '到达'), ('4', '延误'), ('5', '取消')], default='计划', max_length=30)),
                ('plan_departure_time', models.TimeField()),
                ('plan_arrival_time', models.TimeField()),
                ('actual_departure_time', models.TimeField()),
                ('actual_arrival_time', models.TimeField()),
                ('departure', models.CharField(max_length=30)),
                ('arrival', models.CharField(max_length=30)),
                ('punctuality_rate', models.CharField(max_length=30)),
                ('delay_time', models.CharField(max_length=30)),
                ('check_in', models.CharField(max_length=30)),
                ('boarding_port', models.CharField(max_length=30)),
                ('arriving_port', models.CharField(max_length=30)),
                ('Baggage_num', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=20)),
                ('is_mon', models.BooleanField()),
                ('is_tue', models.BooleanField()),
                ('is_wed', models.BooleanField()),
                ('is_thr', models.BooleanField()),
                ('is_fri', models.BooleanField()),
                ('is_sat', models.BooleanField()),
                ('is_sun', models.BooleanField()),
            ],
        ),
    ]
