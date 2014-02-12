from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('math2.views',
	url(r'^$', 'index'),
	url(r'^add/(?P<a>\d+)/(?P<b>\d+)$', 'add'),
	url(r'^factorial/(?P<a>\d+)$', 'factor'),
	url(r'^factorization/(?P<a>\d+)$', 'factorization'),
)
