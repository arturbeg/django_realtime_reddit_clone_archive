# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-20 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interactive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chatgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chatgroup_messages', to='chats.ChatGroup'),
        ),
        migrations.AlterField(
            model_name='message',
            name='globalchat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='globalchat_messages', to='chats.GlobalChat'),
        ),
        migrations.AlterField(
            model_name='message',
            name='localchat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localchat_messages', to='chats.LocalChat'),
        ),
        migrations.AlterField(
            model_name='message',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_messages', to='chats.Topic'),
        ),
    ]
