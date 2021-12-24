import json
import urllib.request
import urllib.error


def import_json(api_url: str):
    """ import url json data

    :param: api_url: External public json url.
    :return: dic Data
    """
    try:
        json_open = urllib.request.urlopen(api_url)
        data = json.load(json_open)
        return data
    except (urllib.error.URLError, urllib.error.HTTPError)  as e:
        # "e" can be treated as a http.client.HTTPResponse object
        print(e)
        return False


def get_songs():

    url_song = "https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json"
    song_data = import_json(url_song)

    song_dict = None

    if song_data:
        song_dict = song_data['feed']['results']

    return song_dict


def get_last_song(limit: int):
    """ Return top song

    :param limit: Cuantity of songs
    :return: list of songs
    """

    list_songs = get_songs()
    if list_songs:
        return list_songs[:limit]
    else:
        return None


def get_genres_data(last_song: list):

    list_genders = []
    list_ids = []
    for song in last_song:

        genres = song.get('genres')

        for genre in genres:
            genre_id = genre.get('genreId')
            genre_name = genre.get('name')

            if str(genre_id) not in list_ids:
                list_ids.append(str(genre_id))
                list_genders.append({str(genre_id): genre_name})

    return list_genders


def get_artist_data(last_song: list):

    list_artist = []
    list_ids = []
    for song in last_song:

        name_artist = song.get('artistName')
        id_artist = song.get('artistId')

        #  for Database simplification cut the origin id for shorter ID
        id_artist = id_artist[:4]

        if str(id_artist) not in list_ids:
            list_ids.append(str(id_artist))
            list_artist.append({str(id_artist): name_artist})

    return list_artist


def get_songs_data(last_song: list):

    list_songs = []
    for song in last_song:

        title = song.get('name')
        release_date = song.get('releaseDate')
        is_explicit = song.get('contentAdvisoryRating')

        if is_explicit:
            is_explicit = True
        else:
            is_explicit = False

        artist_id = song.get('artistId')
        if artist_id:
            #  for Database simplification cut the origin id for shorter ID
            artist_id = artist_id[:4]

        genres = []
        for genre in song.get('genres'):
            genres.append(genre.get('genreId'))

        list_songs.append(
            {
                'title': title,
                'release_date': release_date,
                'explicit': is_explicit,
                'artist_id': artist_id,
                'genres': genre
            }
        )

    return list_songs


def get_list_data():
    """ get list of dict imported data

    :return: List
    """
    last_songs = get_last_song(50)
    songs_format_data = {}

    if last_songs:
        gender_data = get_genres_data(last_songs)
        artist_data = get_artist_data(last_songs)
        songs_data = get_songs_data(last_songs)

        songs_format_data = {
            'genres': gender_data,
            'artists': artist_data,
            'songs': songs_data
        }

    return songs_format_data
