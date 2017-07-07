# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'realPortfolioApp/index.html')

def testimonials(request):
    return render(request, 'realPortfolioApp/testimonials.html')


def about(request):
    return render(request, 'realPortfolioApp/about.html')

def projects(request):
    return render(request, 'realPortfolioApp/projects.html')
