from django.http import HttpResponse
from django.shortcuts import render
from .models import Album


# Create your views here.

def index(request):
    albums_in_db = Album.objects.all()

    context = {'albums_in_db': albums_in_db}

    return render(request, 'music/index.html', context)


def detail(request, album_id):
    return HttpResponse("<h2>Details for album id: " + str(album_id) + " </h2>")
