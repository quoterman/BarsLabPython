from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

def index(request):
    return render(request,"Index.html")

def posts(request):
    post = Post.objects.all()
    return render(request, "posts.html", {"post" : post})

def post(request,post_id):
    post = Post.objects.get(id = post_id)
    return render(request, "post.html", {"post" : post})

def post_new(request):
    return render(request, "newPost.html")

def post_edit(request,post_id):
    return render(request, "post_edit.html", {"post_id" : post_id})

def post_delete(request,post_id):
    return render(request, "post_delete.html", {"post_id" : post_id})