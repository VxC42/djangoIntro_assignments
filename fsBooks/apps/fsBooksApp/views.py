# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Book

def index(request):
    books = Book.objects.all()
    context={"books":books}
    return render(request, "fsBooksApp/index.html", context)

def submit(request):
    Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')
