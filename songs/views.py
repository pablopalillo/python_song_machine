from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework import generics, viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import SongSerializer, SongSaveSerializer, GenreGroupSerializer
from .models import Song, Genre


class SongsView(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'artist__name']

    def list(self, request):

        try:
            queryset = Song.objects.all()
            serializer = SongSerializer(queryset, many=True)
            return Response(serializer.data)

        except ObjectDoesNotExist:
            raise Http404

    def create(self, request):

        song_serializer = SongSaveSerializer(data=request.data)
        if song_serializer.is_valid(raise_exception=True):
            song_serializer.save()
        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_song):

        try:
            song = Song.objects.get(id=id_song)
            song.delete()

            return Response(status.HTTP_200_OK)

        except ObjectDoesNotExist:
            raise Http404


class SongsTopList(generics.ListCreateAPIView):
    """ Get the top 50 songs
    """
    queryset = Song.objects.select_raw_top()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class SongsByGroup(generics.ListCreateAPIView):
    """ View response groups with song related.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreGroupSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
