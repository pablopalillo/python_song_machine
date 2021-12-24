from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import SongSerializer
from .models import Song


class SongsList(generics.ListCreateAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
