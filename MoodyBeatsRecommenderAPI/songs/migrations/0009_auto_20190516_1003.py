# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0008_auto_20190516_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newvideostats',
            name='video_like_count',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
