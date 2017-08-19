# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-03 11:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0004_auto_20170802_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
                ('number_of_members', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ChatGroupMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField()),
                ('chat_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.ChatGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LocalChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=200)),
                ('number_of_favs', models.IntegerField(default=1)),
                ('number_of_active_members', models.IntegerField(default=0)),
                ('chat_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.ChatGroup')),
            ],
        ),
        migrations.CreateModel(
            name='LocalChatMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField()),
                ('local_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.LocalChat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_content', models.TextField()),
                ('created_on', models.DateTimeField()),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('chat_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.ChatGroup')),
                ('local_chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chats.LocalChat')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=200)),
                ('number_of_active_participants', models.IntegerField(default=0)),
                ('chat_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.ChatGroup')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chats.Topic'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]