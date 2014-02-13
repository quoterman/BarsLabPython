from django.conf.urls import patterns, include, url

urlpatterns = patterns('dog.views',
	url(r'^$', 'index'),
)
