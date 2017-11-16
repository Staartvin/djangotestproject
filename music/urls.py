from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # Matches /music/
    url(r'^$', views.index, name='index'),  # Default page
    # Matches /music/albumID/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),  # /music/:albumid
    # Matches /music/albumID/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),  # /music/:albumid
]
