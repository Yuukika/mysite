# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-14 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/images/%Y/%m/%d'),
        ),
    ]
