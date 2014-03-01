


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from univer.models import Group, Student
from django.core.urlresolvers import reverse

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
    return HttpResponseRedirect(
        reverse(details,args=(groupid,))
    )

def student_new(request):
    if request.POST:
        s = Student()
        s.student_name = request.POST["student_name"]
        s.group_id = request.POST["group_id"]
        s.save()
        return HttpResponseRedirect(
            reverse(details,args=(s.group_id,))
        )
    else:
        groups = Group.objects.all()
        return render(request,
                      "univer/student_new.html",
                      {"groups":groups})