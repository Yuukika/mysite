# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-13 08:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180313_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 13, 8, 10, 43, 956729, tzinfo=utc)),
        ),
    ]
