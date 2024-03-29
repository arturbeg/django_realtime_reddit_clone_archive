# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-31 15:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(blank=True, upload_to='group_avatar')),
                ('members', models.ManyToManyField(related_name='is_member', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.SlugField(unique=True)),
                ('chatgroup', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chats.ChatGroup')),
            ],
        ),
        migrations.CreateModel(
            name='LocalChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_private', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, upload_to='local_chat_avatar')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('label', models.SlugField(unique=True)),
                ('chatgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.ChatGroup')),
                ('participants', models.ManyToManyField(related_name='is_participant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(blank=True, max_length=200)),
                ('avatar', models.ImageField(blank=True, upload_to='profile_avatar')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='is_following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_private', models.BooleanField(default=False)),
                ('arrow_ups', models.IntegerField(default=0)),
                ('arrow_downs', models.IntegerField(default=0)),
                ('avatar', models.ImageField(blank=True, upload_to='topic_avatar')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('label', models.SlugField(unique=True)),
                ('chatgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.ChatGroup')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
