# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('secrets', models.ManyToManyField(related_name='likes', to='secretsApp.Secret')),
                ('users', models.ManyToManyField(related_name='likes', to='secretsApp.User')),
            ],
        ),
    ]