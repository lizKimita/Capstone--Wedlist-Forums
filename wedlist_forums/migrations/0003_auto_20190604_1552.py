# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-04 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedlist_forums', '0002_auto_20190604_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post',
        ),
        migrations.AddField(
            model_name='posts',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]