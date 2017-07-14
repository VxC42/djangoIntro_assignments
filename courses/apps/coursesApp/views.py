# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course, Description
import time

def index(request):
    courses = Course.objects.all()
    descriptions = Description.objects.all()
    context={
        "courses":courses,
        "descriptions":descriptions
    }
    return render(request, 'coursesApp/index.html', context)

def add(request):
    course=Course.objects.create(name=request.POST['name'])
    Description.objects.create(description=request.POST['description'], course=course)
    return redirect('/')

def remove(request, id):
    course=Course.objects.get(id=id)
    description=course.description
    print description
    context={
        "course":course,
        "description":description
    }
    return render(request, 'coursesApp/remove.html', context)

def cancel(request):
    return redirect('/')

def delete(request, id):
    course = Course.objects.get(id=id)
    course.description.delete()
    course.delete()
    return redirect('/')
