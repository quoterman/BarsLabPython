from django.http import HttpResponse

def index(request):
    return HttpResponse("INDEX.")

def posts(request):
    return HttpResponse("List of posts")

def post(request,post_id):
    return HttpResponse("Post #"+str(post_id))

def post_new(request):
    return HttpResponse("Adding new post")

def post_edit(request,post_id):
    return HttpResponse("Editing post #" + str(post_id))

def post_delete(request,post_id):
    return HttpResponse("Deleting post #" + str(post_id))