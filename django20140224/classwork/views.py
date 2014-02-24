


from django.http import HttpResponseRedirect
from django.shortcuts import render
from univer.models import Group, Student

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

def student_delete(request, id):
    s = Student.objects.get(id=id)
    groupid = s.group_id
    s.delete()
    return HttpResponseRedirect('/univer/groups/'+str(groupid))