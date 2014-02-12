from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project201402.views.home', name='home'),
    # url(r'^project201402/', include('project201402.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^math/', include('math2.urls')),
	url(r'^dog/', include('dog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	
)
