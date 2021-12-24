from django.urls import path

from . import views

urlpatterns = [
   path('api/import', views.ImportDataView.as_view()),
]
