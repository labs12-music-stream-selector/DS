# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_newvideostats_video_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newvideostats',
            name='video_id',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
    ]