# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-06 07:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wedlist_forums', '0008_auto_20190606_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
                ('voter_id', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='tips',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='tips',
            name='upvote',
        ),
    ]
