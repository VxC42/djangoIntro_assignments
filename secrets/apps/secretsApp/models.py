# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Secret(models.Model):
    secret=models.TextField(max_length=1500)
    user=models.ForeignKey(User, related_name="secrets")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)




class Like(models.Model):
    users=models.ManyToManyField(User, related_name="liked")
    secret=models.ForeignKey(Secret, related_name="likes")
    total_liked = models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
