from django.shortcuts import render
from .models import Album
from django.http import Http404


# Create your views here.

def index(request):
    albums_in_db = Album.objects.all() # Get all albums in the database
    return render(request, 'music/index.html', {'albums_in_db': albums_in_db})


def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("The album with id " + album_id + " does not exist!")
    return render(request, 'music/detail.html', {'album': album})
