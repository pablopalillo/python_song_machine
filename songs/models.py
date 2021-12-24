from django.db import models, DatabaseError
from imports import services


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SongManager(models.Manager):

    def import_data(self):
        self._delete_all()
        data_import = self._get_data_import()

        try:
            self._import_data_genres(data_import)
            self._import_data_artist(data_import)
            self._import_data_songs(data_import)
            return True
        except DatabaseError as e:
            print(e)
            return False

    def _delete_all(self):

        Genre.objects.all().delete()
        Artist.objects.all().delete()
        Song.objects.all().delete()

    def _get_data_import(self):

        data_list = services.get_list_data()
        if data_list:
            return data_list
        else:
            return None

    def _import_data_genres(self, data: dict):
        """ Massive save imported data genres

        :param data: dict
        """
        genres_model_list = []

        if data:
            for key, item in data['genres'].items():

                new_genre = Genre()
                new_genre.id = key
                new_genre.name = item

                genres_model_list.append(new_genre)

            Genre.objects.bulk_create(genres_model_list)

    def _import_data_artist(self, data: dict):
        """ Massive save imported data artists

        :param data: dict
        """
        artist_model_list = []

        if data:
            for key, item in data['artists'].items():

                new_artist = Artist()
                new_artist.id = key
                new_artist.name = item

                artist_model_list.append(new_artist)

            Artist.objects.bulk_create(artist_model_list)

    def _import_data_songs(self, data: dict):
        """ Massive save imported data songs

        :param data: dict
        """
        songs_model_list = []

        if data:
            for item in data['songs']:

                new_song = Song()
                new_song.title = item['title']
                new_song.release_date = item['release_date']
                new_song.explicit = item['explicit']

                songs_model_list.append(new_song)

            Song.objects.bulk_create(songs_model_list)


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    explicit = models.BooleanField(null=True)
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre)
    object = SongManager()

    def __str__(self):
        return self.title
