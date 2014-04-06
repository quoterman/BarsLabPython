
from django.conf.urls import url, patterns
from django.views.generic import TemplateView, DetailView
from twitter.models import Tweet
from analytics.views import TweetListView, CurrentUserTweetListView, TweetInfoView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', TweetListView.as_view()),
    url(r'^page(?P<page>\d+)$', TweetListView.as_view()),

    url(r'^my/$', CurrentUserTweetListView.as_view()),
    url(r'^my/page(?P<page>\d+)$', CurrentUserTweetListView.as_view()),

    url(r'^home$', 
    	TemplateView.as_view(template_name="analytics/dashboard.html")),

    url(r'^tweetinfo/(?P<pk>\d+)$', TweetInfoView.as_view())

    #url(r'^tweetinfo/(?P<pk>\d+)$', DetailView.as_view(model=Tweet,
    #	template_name="analytics/tweetinfo.html"))
)