from django.http import HttpResponse
import math

def index(request):
	return HttpResponse('Hello')
	
def add(request,a,b):
	return HttpResponse(str(int(a) + int(b)))
	
def factor(request,a):
	return HttpResponse(math.factorial(int(a)))
	
def factorization(request,a):
	i = 2
	s = ''
	temp = int(a)
	while( temp != 1):
		if temp % i == 0:
			s = s + str(i) + " "
			temp = temp / i
		else:
			i = i + 1
	return HttpResponse(str(s))		