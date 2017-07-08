# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, "surpriseMeApp/index.html")

def results(request):
    values=['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'gold', 'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'xray', 'yankee', 'zulu']
    display=[]
    wordsToPost=request.POST['number']
    for x in range(0, int(wordsToPost)):
        display.append(random.choice(values))

    context={
        'results':display
    }

    return render(request, "surpriseMeApp/results.html", context)
