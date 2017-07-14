# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from validations import formIsValid
from .models import User

def index(request):
    return render(request, 'validationApp/index.html')


def submit(request):
    state = formIsValid(request.POST['username'])

    if (state['isValid']==True):
        User.objects.create(username=request.POST['username'])
        users = User.objects.all()
        context={
            "users":users
        }
        return render(request, 'validationApp/success.html', context)
    else:
        context={
            "error":"Username is not valid!"
        }
        return render(request, 'validationApp/index.html', context)

def delete(request, id):
    User.objects.get(id=id).delete()
    return redirect('/')
