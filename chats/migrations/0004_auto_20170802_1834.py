# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-02 18:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20170801_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgroupmembership',
            name='chat_group',
        ),
        migrations.RemoveField(
            model_name='chatgroupmembership',
            name='user',
        ),
        migrations.RemoveField(
            model_name='chatgrouprating',
            name='chat_group',
        ),
        migrations.RemoveField(
            model_name='localchat',
            name='chat_group',
        ),
        migrations.RemoveField(
            model_name='localchatmembership',
            name='sub_chat',
        ),
        migrations.RemoveField(
            model_name='localchatmembership',
            name='user',
        ),
        migrations.RemoveField(
            model_name='localchatrating',
            name='permanent_chat_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat_group',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sub_chat',
        ),
        migrations.RemoveField(
            model_name='message',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='chat_group',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userrating',
            name='chat_group',
        ),
        migrations.RemoveField(
            model_name='userrating',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChatGroup',
        ),
        migrations.DeleteModel(
            name='ChatGroupMembership',
        ),
        migrations.DeleteModel(
            name='ChatGroupRating',
        ),
        migrations.DeleteModel(
            name='LocalChat',
        ),
        migrations.DeleteModel(
            name='LocalChatMembership',
        ),
        migrations.DeleteModel(
            name='LocalChatRating',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='UserRating',
        ),
    ]
