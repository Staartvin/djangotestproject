from django.conf.urls import url
from . import views

urlpatterns = [
    # Matches /music/
    url(r'^$', views.index, name='index'),  # Default page
    # Matches /music/albumID/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),  # /music/:albumid
]
