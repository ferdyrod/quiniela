from django.conf.urls import patterns, include, url

from predicciones.views import *

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
)
    