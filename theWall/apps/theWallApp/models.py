# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeNow(auto_now_add=True)
    updated_at=models.DateTimeNow(auto_now=True)

class Message(models.Model):
    user_id = models.ForeignKey(User)
    message = models.TextField(max_length=1000)
    created_at=models.DateTimeNow(auto_now_add=True)
    updated_at=models.DateTimeNow(auto_now=True)

class Comment(models.Model):
    message_id=models.ForeignKey(Message)
    user_id=models.ForeignKey(User)
    comment=models.TextField(max_length=1000)
    created_at=models.DateTimeNow(auto_now_add=True)
    updated_at=models.DateTimeNow(auto_now=True)
