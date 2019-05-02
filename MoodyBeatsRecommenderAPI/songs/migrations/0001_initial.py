# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-01 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songs', models.CharField(blank=True, max_length=200, null=True)),
                ('song_embed_code', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('recommendation_one', models.CharField(blank=True, max_length=140, null=True)),
                ('recommendation_two', models.CharField(blank=True, max_length=140, null=True)),
                ('recommendation_three', models.CharField(blank=True, max_length=140, null=True)),
                ('recommendation_four', models.CharField(blank=True, max_length=140, null=True)),
                ('recommendation_five', models.CharField(blank=True, max_length=140, null=True)),
            ],
        ),
    ]