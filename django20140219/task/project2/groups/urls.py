__author__ = 'Artur'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$','groups.views.index'),
    url(r'^(?P<id>\d+)','groups.views.details'),
)