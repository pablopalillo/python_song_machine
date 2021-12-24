from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from songs.models import Song


class ImportDataView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):

        try:

            Song.object.import_data()

        except ObjectDoesNotExist:
            raise Http404

        return Response(status=status.HTTP_201_CREATED)