from django.urls import path

from . import views

urlpatterns = [
   path(
      'api/songs',
      views.SongsView.as_view({'get': 'list', 'post': 'create'}),
      name="Retrieve Songs"
   ),
   path('api/songs/top', views.SongsTopList.as_view()),
]
