from django.urls import path

from . import views

urlpatterns = [
   path(
      'api/songs',
      views.SongsView.as_view({'get': 'list', 'post': 'create'}),
      name="API Songs"
   ),
   path(
      'api/song/<int:id_song>',
      views.SongsView.as_view({'delete': 'delete'}),
      name="Delete Song"
   ),
   path('api/songs/top', views.SongsTopList.as_view()),
]
