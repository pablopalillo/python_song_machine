from django.urls import path

from . import views

urlpatterns = [
   path('import', views.ImportDataView.as_view()),
]
