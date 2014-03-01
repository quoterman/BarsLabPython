

from django.conf.urls import patterns, include, url

urlpatterns = patterns('univer.views',
    url(r'^groups$', 'index', name='groups'),
    url(r'^groups/(?P<id>\d+)$','details', name='groups_details'),
    #url(r'^students$', 'students'),
    #url(r'^students/(?P<id>\d+)$', 'student'),
	url(r'^students/(?P<id>\d+)/delete$', 'student_delete', name='student_delete'),
    url(r'^students/new$', 'student_new', name='student_new'),
)
