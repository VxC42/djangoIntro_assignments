from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.index),
    url(r'^process$', views.process, name='process'),
    url(r'^result$', views.result),
    url(r'^goback$', views.index)
]
