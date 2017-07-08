# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse('No Ninjas Here')

def all(request):
    context={
        "displayAll":True
    }
    return render(request, 'disappearingNinjaApp/ninjas.html', context)

def ninjas(request, color):

    if color == 'blue' or color =='red' or color=='purple' or color=='orange':
        context={
            'displayAll':False,
            'color':color
        }
        print color
    else:
        context={
            'displayAll':False
        }
    return render(request, 'disappearingNinjaApp/ninjas.html', context)
