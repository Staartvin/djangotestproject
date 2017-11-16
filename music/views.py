from django.shortcuts import render, get_object_or_404
from .models import Album


# Create your views here.

def index(request):
    albums_in_db = Album.objects.all() # Get all albums in the database
    return render(request, 'music/index.html', {'albums_in_db': albums_in_db})


def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/detail.html', {'album': album})


