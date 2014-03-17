from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from twitter.models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from twitter.decorators import no_login_please

import datetime
from twitter.forms import TweetForm, LoginForm, UserSettingsForm

@login_required
def home(request):
	if request.method == "POST":
		f = TweetForm(request.POST)
		if f.is_valid():
			t = Tweet()
			t.user = request.user
			t.text = f.cleaned_data["text"]
			t.published_on = datetime.datetime.today()
			t.save()
		else:
			tweets = Tweet.objects.order_by("-published_on")[:5]
			return render(request,'twitter/home.html', {"tweets":tweets, 
			"f": f})
	else:
		f = TweetForm()
		tweets = Tweet.objects.order_by("-published_on")[:5]
		return render(request,'twitter/home.html', {"tweets":tweets, 
			"f": f})

@no_login_please
def log_in(request):
	if request.POST:
		f = LoginForm(request.POST)
		if f.is_valid():
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				if request.GET.has_key("next"):
					redirect_path = request.GET["next"]
				else:
					redirect_path = reverse('twitter:home')
				return HttpResponseRedirect(redirect_path)
			else:
				return HttpResponseRedirect(reverse('twitter:login'))
		else:
			if request.GET.has_key("next"):
				context = {'next': request.GET["next"]}
			else:
				context = {}	
			context["f"] = f
			return render(request,'twitter/login.html', context)						
	else:
		if request.GET.has_key("next"):
			context = {'next': request.GET["next"]}
		else:
			context = {}
		f = LoginForm()
		context["f"] = f
		return render(request,'twitter/login.html', context)


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


@login_required
def settings(request):
	if request.method == "POST":
		f = UserSettingsForm(request.POST)
		if f.is_valid():
			request.user.first_name = f.cleaned_data["first_name"]
			request.user.last_name = f.cleaned_data["last_name"]
			request.user.email = f.cleaned_data["email"]
			request.user.save()
			return HttpResponseRedirect(reverse("twitter:home"))
		else:
			return render(request,"twitter/settings.html",{"f":f})

	else:
		f = UserSettingsForm(instance=request.user)
		return render(request,"twitter/settings.html",{"f":f})