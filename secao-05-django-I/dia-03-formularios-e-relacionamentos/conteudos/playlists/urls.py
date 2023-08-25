from django.urls import path
from playlists.views import index, singer, music


urlpatterns = [
    path("", index, name="home-page"),
    path("singers/", singer, name="singers-page"),
    path("musics/", music, name="musics-page"),
]
