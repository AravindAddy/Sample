# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_type',
            new_name='song_title',
        ),
    ]
