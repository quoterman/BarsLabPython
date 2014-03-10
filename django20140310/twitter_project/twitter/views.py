from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from twitter.models import Tweet
from django.contrib.auth.models import User
import datetime

def tweet(request):
	if request.user.is_authenticated():
		t = Tweet()
		t.user = request.user
		t.text = request.POST["text"]
		t.published_on = datetime.datetime.today()
		t.save()
		return HttpResponseRedirect(reverse('twitter:home'))
	else:
		return HttpResponseRedirect(reverse('twitter:login'))


def home(request):
	if request.user.is_authenticated():
		tweets = Tweet.objects.order_by("-published_on")[:5]
		return render(request,'twitter/home.html', {"tweets":tweets})
	else:
		return HttpResponseRedirect(reverse('twitter:login'))

def log_in(request):
	if request.user.is_anonymous():
		if request.POST:
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect(reverse('twitter:home'))
			else:
				return HttpResponseRedirect(reverse('twitter:login'))
		else:
			return render(request,'twitter/login.html')
	else:
		return HttpResponseRedirect(reverse('twitter:home'))


def log_out(request):
	if request.user.is_authenticated():
		logout(request)	
	
	return HttpResponseRedirect(reverse('twitter:login'))

def registration(request):
	if request.user.is_anonymous():
		if request.POST:
			username = request.POST["username"]
			password = request.POST["password"]
			password2 = request.POST["password2"]
			email = request.POST["email"]

			u = User.objects.filter(username=username)
			if u:
				return render(request,'twitter/registration.html',
							{"error_message":"Choose another username"})

			u = User.objects.filter(email=email)

			if u:
				return render(request,'twitter/registration.html',
							{"error_message":"Choose another email"})	

			if (password!=password2):
				return render(request,'twitter/registration.html',
							{"error_message":"Passwords do not match"})	

			u = User.objects.create_user(username=username,
				email=email,password=password)
			u.save()
			return log_in(request)			

		else:
			return render(request,'twitter/registration.html')
	else:
		return HttpResponseRedirect(reverse('twitter:home'))