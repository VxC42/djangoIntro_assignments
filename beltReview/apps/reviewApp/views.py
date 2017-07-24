# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from validations import formIsValid, loginIsValid, emailExists, usernameExists
from models import User, Book, Review

def index(request):
    return render(request, 'reviewApp/index.html')


def register(request):
    state=formIsValid(request.POST)
    emailState=emailExists(request.POST)
    usernameState=usernameExists(request.POST)
    if emailState['exists']:
        errors = emailState['errors']
        context={
            'errors':errors
        }
        return render(request, "reviewApp/index.html", context)
    elif usernameState['exists']:
        errors = usernameState['errors']
        context={
            'errors':errors
        }
        return render(request, "reviewApp/index.html", context)
    else:
        if state['isValid']:
            user=User.objects.create(name=request.POST['name'], username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            request.session['user']=request.POST['email']
            return redirect("/books")
        else:
            errors =  state['errors']
            context={
                'errors':errors
            }
            return render(request, "reviewApp/index.html", context)
    return render(request, 'reviewApp/books.html')

def login(request):
    state=loginIsValid(request.POST)
    if state['isValid']:
        checkUser = User.objects.filter(email=request.POST['email'])
        if checkUser.count()==0:
            errors=['No such account']
            context={
                'errors':errors
            }
            return render(request, "reviewApp/index.html", context)
        else:
            getUser= User.objects.get(email=request.POST['email'])
            if request.POST['password']==getUser.password:
                request.session['user']=request.POST['email']
                return redirect("/books")
            else:
                errors=['Password Does Not Match Account']
                context={
                    'errors':errors
                }
                return render(request, "reviewApp/index.html", context)
    else:
        errors =  state['errors']
        context={
            'errors':errors
        }
        return render(request, "reviewApp/index.html", context)
    return render(request, 'reviewApp/books.html')

def books(request):
    user=User.objects.get(email=request.session['user'])
    books = Book.objects.all()
    reviews = Review.objects.all().order_by('-created_at')
    context={
        'user':user,
        'books':books,
        'reviews':reviews
    }

    return render(request, 'reviewApp/books.html', context)

def add(request):
    authors=Book.objects.all()
    context={
        'authors':authors
    }
    return render(request, 'reviewApp/add.html', context)

def addBook(request):
    errors=[]
    user=User.objects.get(email=request.session['user'])
    title=request.POST['title']
    if request.POST['authorType']:
        author=request.POST['authorType']
    else:
        author=request.POST['authorSelect']
    review=request.POST['review']
    rating=request.POST['rating']
    if len(title)==0 or len(author)==0 or len(review)==0:
        errors.append("all fields must be filled out")
        context={
            'errors':errors
        }
        print "here"
        return render(request, 'reviewApp/add.html', context)
    else:
        checkBook=Book.objects.filter(title=title, author=author)
        if len(checkBook)==0:
            this_book = Book.objects.create(title=title, author=author)
            Review.objects.create(rating=rating, review=review, users=user, books=this_book)
        else:
            getBook=Book.objects.get(title=title, author=author)
            Review.objects.create(rating=rating, review=review, users=user, books=getBook)

        return redirect('/books')

def userPage(request, id):
    user=User.objects.get(id=id)
    reviews=Review.objects.filter(users=user)
    context={
        'user':user,
        'reviews':reviews,
    }
    return render(request, 'reviewApp/users.html', context)

def bookPage(request, id):
    user=User.objects.get(email=request.session['user'])
    book=Book.objects.get(id=id)
    reviews=Review.objects.filter(books=book)
    context={
        'book':book,
        'reviews':reviews,
        'user':user
    }

    return render(request, 'reviewApp/book.html', context)


def delete(request, id):
    this_review=Review.objects.get(id=id)
    this_book=this_review.books.id
    this_review.delete()
    return redirect('/book/'+ this_book)


def logout(request):
    request.session['user']=None
    return render(request, 'reviewApp/index.html')
