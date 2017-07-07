# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random, string


def index(request):
        if 'attempt' not in request.session:
            request.session['attempt']=0
        context={
            "attempt": request.session['attempt']
        }
        return render(request, "randomWordApp/index.html", context)

def generate(request):
    request.session['attempt']+=1
    num = request.session['attempt']
    if request.method=="POST":
        randomstring = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)])
        context={
            'random':randomstring,
            'attempt':request.session['attempt']
        }
        return render(request, "randomWordApp/index.html", context)
    else:
        return render(request, "randomWordApp/index.html")
