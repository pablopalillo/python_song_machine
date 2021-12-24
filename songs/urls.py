from django.urls import path

from . import views

urlpatterns = [
   path('api/songs', views.SongsList.as_view()),
]
