# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Review(models.Model):
    rating=models.FloatField(default=0)
    review=models.TextField(max_length=2000)
    users=models.ForeignKey(User)
    books=models.ForeignKey(Book, related_name="reviews")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
