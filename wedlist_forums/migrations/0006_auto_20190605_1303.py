# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-05 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedlist_forums', '0005_auto_20190605_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tips',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='tips',
            name='tipper_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tips',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
