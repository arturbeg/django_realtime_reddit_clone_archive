# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-10 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0017_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]