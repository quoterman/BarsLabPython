from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'index'),
    url(r'^posts$', 'posts'),
    url(r'^posts/(?P<post_id>\d+)$', 'post'),
    url(r'^posts/new$', 'post_new'),
    url(r'^posts/(?P<post_id>\d+)/edit$', 'post_edit'),
    url(r'^posts/(?P<post_id>\d+)/delete$', 'post_delete'),
)
