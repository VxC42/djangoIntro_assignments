from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^add$', views.add),
    url(r'^addBook$', views.addBook),
    url(r'^logout$', views.logout),
    url(r'^book/(?P<id>\d+)', views.bookPage),
    url(r'^delete/(?P<id>\d+)', views.delete),
    url(r'^user/(?P<id>\d+)', views.userPage),
]
