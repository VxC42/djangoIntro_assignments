# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from validations import formIsValid, loginIsValid
from .models import User

def index(request):
    return render(request, "loginRegApp/index.html")

def login(request):
    state = loginIsValid(request.POST)
    if state['isValid']:
        getUser = User.objects.get(email=request.POST['email'])
        if request.POST['pw']==getUser.password:
            context={
                'user':getUser
            }
            print 'Success'
            return render(request, "loginRegApp/success.html", context)
        else:
            print 'error wrong pw'
            return redirect('/')
    else:
        errors =  state['errors']
        context={
            'errors':errors
        }
        return render(request, "loginRegApp/index.html", context)

def register(request):
    state=formIsValid(request.POST)
    if state['isValid']:
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['pw'])
        context={
            'user':user
        }
        print 'registered!'
        return render(request, "loginRegApp/success.html", context)
    else:
        errors =  state['errors']
        context={
            'errors':errors
        }
        return render(request, "loginRegApp/index.html", context)
