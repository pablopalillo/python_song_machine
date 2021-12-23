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
    :return: Dic of songs
    """

    list_songs = get_songs()
    if list_songs:
        return list_songs[:limit]
    else:
        return None
