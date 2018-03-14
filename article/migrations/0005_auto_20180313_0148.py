# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-13 01:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0004_auto_20180312_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='article_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 13, 1, 48, 20, 33431, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='articlepost',
            name='articel_tag',
            field=models.ManyToManyField(related_name='article_tag', to='article.article_tag'),
        ),
    ]
