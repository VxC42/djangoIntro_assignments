# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 05:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretsApp', '0007_auto_20170720_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_liked', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='secret',
            name='likes',
        ),
        migrations.AddField(
            model_name='like',
            name='secret',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretsApp.Secret'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ManyToManyField(related_name='likes', to='secretsApp.User'),
        ),
    ]