from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def home(request):
	if request.user.is_authenticated():
		return HttpResponse("Welcome, " + str(request.user) + "!")
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
