from django.shortcuts import render
from posts.models import Musician, Album

def home(request):
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    return render(request, 'home.html', {'musicians' : musicians, 'albums': albums})