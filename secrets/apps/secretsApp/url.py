from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^secrets$', views.secrets),
    url(r'^postSecret/(?P<id>\d+)$', views.postSecret),
    url(r'^like/(?P<secretid>\d+)$', views.like),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^popular$', views.popular),
]
