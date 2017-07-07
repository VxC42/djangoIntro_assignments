# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    context={
        "date": datetime.datetime.now().strftime('%B %d, %Y %H:%M %p'),
        }
    return render(request, "timeDisplayApp/index.html", context)
