__author__ = 'Artur'

from django.conf.urls import patterns, include, url
urlpatterns = patterns('Foutball.views',
    url(r'^$', 'index', name='index')
)

