# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-10 08:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180310_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 10, 8, 30, 2, 622897, tzinfo=utc)),
        ),
    ]