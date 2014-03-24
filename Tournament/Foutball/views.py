from django.shortcuts import render
from Foutball.models import Match

def index(request):
    match = Match.objects.all()
    return render(request, 'index.html', {'match': match})
