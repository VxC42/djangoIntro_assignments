# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.shortcuts import render, HttpResponse, redirect


def index(request):

    return render(request, 'surveyFormApp/index.html')

def process(request):
    if 'submission' not in request.session:
        request.session['submission']=0
    request.session['name'] = request.POST['name']
    request.session['dojo']=request.POST['dojo']
    request.session['language']=request.POST['language']
    request.session['comment']=request.POST['comment']

    return redirect('/result')

def result(request):
    request.session['submission']+=1
    context={
        "name": request.session['name'],
        "dojo": request.session['dojo'],
        "language": request.session['language'],
        "comment": request.session['comment'],
        "num":request.session['submission']
    }
    return render(request, 'surveyFormApp/result.html', context)

def goback(request):
    return render(request, 'surveyFormApp/index.html')
