# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-01 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
