from rest_framework import serializers
from .models import Song, Artist, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['id']


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'
        read_only_fields = ['id']


class SongSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True, read_only=True)
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'release_date', 'explicit', 'artist', 'genres']
        read_only_fields = ['id']


class SongSaveSerializer(serializers.ModelSerializer):

    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.only("id"))
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.only("id"), many=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'release_date', 'explicit', 'artist', 'genres']
        read_only_fields = ['id']
