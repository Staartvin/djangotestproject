from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # Matches /music/
    url(r'^$', views.IndexView.as_view(), name='index'),  # Default page

    # Matches /music/albumID/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),  # /music/:albumid

    # Matches /music/album/add/
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # Matches /music/album/:albumID/edit/
    url(r'^album/(?P<pk>[0-9]+)/edit$', views.AlbumUpdate.as_view(), name='album-edit'),

    # Matches /music/album/albumID/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete', views.AlbumDelete.as_view(), name='album-delete'),

]
