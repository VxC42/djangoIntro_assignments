# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import datetime


def randomNum(start, end):
    num = random.randrange(start, end)
    return num

def addEvent(request, num, building):
    timestamp = datetime.datetime.now().strftime("%Y/%m/%d %H:%M %p")
    if not request.session.get('event', None):
        event = []
    else:
        event = request.session['event']
    if building == 'casino':
        if num<0:
            event.append('Entered a casino and lost ' +str(num)+ 'gold... Ouch.. ' + '('+str(timestamp)+')')

        else:
            event.append('Entered a casino and won ' +str(num)+ ' gold! ' + '('+str(timestamp)+')')
    else:
        event.append('Earned ' +str(num)+ ' from the '+building+'! ' + '('+str(timestamp)+')')
        request.session['event']=event
        print event


def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'event' not in request.session:
        request.session['event']=None
    context={
        "gold":request.session['gold'],
        "events":request.session['event']
    }
    return render(request, 'ninjaGoldApp/index.html', context)

def process_money(request):
    if request.POST['building']=='farm':
        goldEarned = randomNum(10,21)
        request.session['gold'] +=goldEarned
        addEvent(request, goldEarned, 'farm')
    elif request.POST['building']=='cave':
        goldEarned = randomNum(5,11)
        request.session['gold'] +=goldEarned
        addEvent(request, goldEarned, 'cave')
    elif request.POST['building']=='house':
        goldEarned = randomNum(2,6)
        request.session['gold'] +=goldEarned
        addEvent(request, goldEarned, 'house')
    elif request.POST['building']=='casino':
        goldEarned = randomNum(-50,51)
        request.session['gold'] +=goldEarned
        addEvent(request, goldEarned, 'casino')
    return redirect('/')


def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
