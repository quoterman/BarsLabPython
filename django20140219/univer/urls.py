from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'univer.views.index'),
    url(r'^(?P<id>\d+)','univer.views.details'),
)