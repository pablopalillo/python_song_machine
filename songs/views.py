from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .serializers import SongSerializer
from .models import Song


class SongsList(generics.ListCreateAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'artist__name']


class SongsTopList(generics.ListCreateAPIView):
    """ Get the top 50 songs
    """
    queryset = Song.objects.select_raw_top()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
