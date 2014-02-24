

from django.conf.urls import patterns, include, url

urlpatterns = patterns('univer.views',
    url(r'^groups$', 'index'),
    url(r'^groups/(?P<id>\d+)$','details'),
    #url(r'^students$', 'students'),
    #url(r'^students/(?P<id>\d+)$', 'student'),
	url(r'^students/(?P<id>\d+)/delete$', 'student_delete'),
)
