from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/?$', views.register),
    url(r'^login/?$', views.login),
    url(r'^success/?$', views.success),
    url(r'^logoff/?$', views.logoff),
]