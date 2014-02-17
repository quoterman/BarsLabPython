from django.http import HttpResponse


def groups(request):
    return HttpResponse("groups")

def group_list(request,group_id):
    return HttpResponse("group #" + group_id)
