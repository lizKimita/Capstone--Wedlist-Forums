# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-04 12:46
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('wedlist_forums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='description',
        ),
        migrations.AddField(
            model_name='posts',
            name='post',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]