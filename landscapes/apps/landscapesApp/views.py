# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    context={
        'title':'Welcome! Enter any number 1-50 as a url parameter, for example "/32"'
    }
    return render(request, "landscapesApp/index.html", context)

def num(request, num):
    intnum = int(num)
    context={
        'num':intnum,
        'error':'WAIT! Please enter a number between 1-50!'
        }
    return render(request, "landscapesApp/num.html", context)
