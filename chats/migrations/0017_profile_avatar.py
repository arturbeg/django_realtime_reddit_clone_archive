# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-10 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0016_auto_20170810_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profile_avatar'),
        ),
    ]