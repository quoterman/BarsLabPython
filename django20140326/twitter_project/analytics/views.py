from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from twitter.models import Tweet

class TweetListView(ListView):
	model = Tweet
	template_name = "analytics/tweetlist.html"
	context_object_name = "tweets"
	paginate_by = 5

	def get_queryset(self):
		tweets = Tweet.objects.all().order_by("-published_on")
		return tweets

class CurrentUserTweetListView(TweetListView):
	paginate_by = 7
	def get_queryset(self):
		tweets = \
			Tweet.objects.filter(user=self.request.user).order_by("-published_on")
		return tweets

class TweetInfoView(DetailView):
	model = Tweet
	template_name = "analytics/tweetinfo.html"
	def get_context_data(self, **kwargs):
		context = super(TweetInfoView,self).get_context_data(**kwargs)
		tweets = Tweet.objects.filter(published_on__lt=self.object.published_on).order_by("-published_on")[:2]
		context["beforetweets"] = tweets
		return context