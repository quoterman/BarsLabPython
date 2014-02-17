from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("INDEX.")

def posts(request):
    return render(request, "1.html")
    #return HttpResponse("List of posts")

def post(request,post_id):
    n = int(post_id)
    friends = []
    for i in range(n):
        friends.append(i)
    return render(request, "post.html", {"friends" : friends})


def post_new(request):
    return HttpResponse("Adding new post")

def post_edit(request,post_id):
    return HttpResponse("Editing post #" + str(post_id))

def post_delete(request,post_id):
    return HttpResponse("Deleting post #" + str(post_id))