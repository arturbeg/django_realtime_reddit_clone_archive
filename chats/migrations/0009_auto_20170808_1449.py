# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-08 14:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0008_auto_20170808_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]