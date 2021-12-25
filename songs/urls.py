from django.urls import path

from . import views

urlpatterns = [
   path('api/songs', views.SongsList.as_view()),
   path('api/songs/top', views.SongsTopList.as_view()),
]
