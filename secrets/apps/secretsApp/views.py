# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from validations import formIsValid, loginIsValid
from .models import User, Secret, Like
import datetime
from pytz import timezone


def index(request):
    return render(request, "secretsApp/index.html")

def register(request):
    state=formIsValid(request.POST)
    if state['isValid']:
        user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['user']=request.POST['email']
        return redirect("/secrets")
    else:
        errors =  state['errors']
        context={
            'errors':errors
        }
        return render(request, "secretsApp/index.html", context)

def login(request):
    state=loginIsValid(request.POST)
    if state['isValid']:
        checkUser = User.objects.filter(email=request.POST['email'])
        if checkUser.count()==0:
            errors=['No such account']
            context={
                'errors':errors
            }
            return render(request, "secretsApp/index.html", context)
        else:
            getUser= User.objects.get(email=request.POST['email'])
            if request.POST['password']==getUser.password:
                request.session['user']=request.POST['email']
                return redirect("/secrets")
            else:
                errors=['Password Does Not Match Account']
                context={
                    'errors':errors
                }
                return render(request, "secretsApp/index.html", context)
    else:
        errors =  state['errors']
        context={
            'errors':errors
        }
        return render(request, "secretsApp/index.html", context)


def secrets(request):
    email=request.session['user']
    user=User.objects.get(email=request.session['user'])
    secrets=Secret.objects.all().order_by('-created_at')
    likes = Like.objects.all()
    current_time = datetime.datetime.now()
    current_state=[]
    for secret in secrets:
        current_state.append((secret, liked(secret, user)))

    print secrets
    context={
        'secrets':secrets,
        'user':user,
        'likes':likes,
        'time':current_time,
        'secLikes':current_state
    }

    return render(request, "secretsApp/secrets.html", context)

def liked(secret, user):
    try:
        user_liked = Like.objects.get(secret=secret, users=user)
    except:
        user_liked = None
    if user_liked:
        return True
    else:

        return False

def postSecret(request, id):
    secret=request.POST.get('secret')
    this_secret = Secret.objects.create(secret=secret, user=User.objects.get(id=id))
    this_like = Like.objects.create(secret=this_secret, total_liked=0)
    return redirect('/secrets')

def like(request, secretid):
    secret=Secret.objects.get(id=secretid)
    # print secret.secret
    user=User.objects.get(email=request.session['user'])
    # print user.first_name, secret.user.first_name
    likepressed=Like.objects.filter(secret=secret)

    if Like.objects.filter(users=user, secret=secret):
        likepressed=Like.objects.get(users=user, secret=secret)
        likepressed.users.remove(user)
        likepressed.total_liked-=1
        likepressed.save()
    else:
        likepressed=Like.objects.get(secret=secret)
        likepressed.users.add(user)
        likepressed.total_liked+=1
        likepressed.save()


    return redirect('/secrets')


def delete(request, id):
    Secret.objects.get(id=id).delete()
    return redirect('/secrets')

def checkUser(user, secret):
    isUsers=False
    sEmail= secret.user.email
    uEmail= user.email
    if uEmail == sEmail:
        isUsers=True
    else:
        isUsers=False
    return isUsers

def popular(request):
    user=User.objects.get(email=request.session['user'])
    secrets=Like.objects.all().order_by('-total_liked')
    ordered=Like.objects.all()
    likes = Like.objects.all()
    current_state=[]

    for secret in secrets:
        current_state.append((secret.secret, liked(secret.secret, user)))


    context={
        'user':user,
        'secrets':secrets,
        'likes':likes,
        'secLikes':current_state,

    }
    return render(request, 'secretsApp/popular.html', context)


# secrets=Secret.objects.all().order_by('-created_at')

# for secret in secrets:
#     is_liked=Like.objects.filter(users=user, secret=secret).exists()
#     state = is_liked
