from django.http import HttpResponse
from django.shortcuts import render
from univer.models import Group

def index(request):
    groups = Group.objects.all()
    return render(request,
                  "univer/index.html",
                  {"groups" : groups}
    )

def details(request, id):
    group = Group.objects.get(id=id)
    return render(request,
                  "univer/details.html",
                  {"group" : group}
    )