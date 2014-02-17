from django.conf.urls import patterns, include, url

urlpatterns = patterns('groups.views',
    url(r'^$',"groups"),
    url(r'(?P<group_id>11-(\d+))', "group_list"),

)
