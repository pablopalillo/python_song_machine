from django.db import models


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


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    explicit = models.BooleanField(null=True)
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre)
