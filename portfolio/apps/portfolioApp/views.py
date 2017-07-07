# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'portfolioApp/index.html')

def testimonials(request):
    print request.method
    return render(request, 'portfolioApp/testimonials.html')
