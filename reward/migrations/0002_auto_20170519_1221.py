# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-19 12:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reward',
            old_name='commentTime',
            new_name='rewardTime',
        ),
    ]
