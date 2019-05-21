# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_remove_newcomment_moods'),
    ]

    operations = [
        migrations.AddField(
            model_name='newvideo',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newvideo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]