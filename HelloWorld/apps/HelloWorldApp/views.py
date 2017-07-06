# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
  print "Hello World"
  return render(request, 'HelloWorldApp/index.html')
