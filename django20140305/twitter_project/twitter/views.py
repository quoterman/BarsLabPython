from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from twitter.models import Tweet
import datetime

def tweet(request):
	if request.user.is_authenticated():
		t = Tweet()
		t.user = request.user
		t.text = request.POST["text"]
		t.published_on = datetime.datetime.today()
		t.save()
		return HttpResponseRedirect(reverse(home))
	else:
		return HttpResponseRedirect(reverse(log_in))


def home(request):
	if request.user.is_authenticated():
		tweets = Tweet.objects.order_by("-published_on")[:5]
		return render(request,'twitter/home.html', {"tweets":tweets})
	else:
		return HttpResponseRedirect(reverse(log_in))

def log_in(request):
	if request.user.is_anonymous():
		if request.POST:
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect(reverse(home))
			else:
				return HttpResponseRedirect(reverse(log_in))
		else:
			return render(request,'twitter/login.html')
	else:
		return HttpResponseRedirect(reverse(home))


def log_out(request):
	if request.user.is_authenticated():
		logout(request)	
	
	return HttpResponseRedirect(reverse(log_in))