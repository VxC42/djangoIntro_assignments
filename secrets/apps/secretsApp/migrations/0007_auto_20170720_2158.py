# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretsApp', '0006_auto_20170720_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='secret',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='secret',
            name='likes',
            field=models.ManyToManyField(to='secretsApp.User'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
