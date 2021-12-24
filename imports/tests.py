from django.test import TestCase
from .services import import_json, get_songs, get_last_song, get_genres_data, get_artist_data, get_songs_data


class TestServicesImport(TestCase):

    url_song = "https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json"
    song_data = []

    def setUp(self):
        self.song_data = [
                {
                    "artistName": "Kodak Black",
                    "id": "1592774398",
                    "name": "Super Gremlin",
                    "releaseDate": "2021-10-30",
                    "kind": "songs",
                    "artistId": "953921140",
                    "artistUrl": "https://music.apple.com/us/artist/kodak-black/953921140",
                    "contentAdvisoryRating": "Explict",
                    "artworkUrl100": "https://is2-ssl.mzstatic.com/image/thumb/Music126/v4/6b/3b/fc/6b3bfc34-cdce-b3ef-db0f-caa4b760dd0b/075679764195.jpg/100x100bb.jpg",
                    "genres": [
                        {
                            "genreId": "18",
                            "name": "Hip-Hop/Rap",
                            "url": "https://itunes.apple.com/us/genre/id18"
                        },
                        {
                            "genreId": "34",
                            "name": "Music",
                            "url": "https://itunes.apple.com/us/genre/id34"
                        }
                    ],
                    "url": "https://music.apple.com/us/album/super-gremlin/1592774394?i=1592774398"
                },
                {
                    "artistName": "Lil Durk",
                    "id": "1600722156",
                    "name": "Broadway Girls (feat. Morgan Wallen)",
                    "releaseDate": "2021-12-19",
                    "kind": "songs",
                    "artistId": "541282483",
                    "artistUrl": "https://music.apple.com/us/artist/lil-durk/541282483",
                    "artworkUrl100": "https://is4-ssl.mzstatic.com/image/thumb/Music116/v4/6f/73/de/6f73de5d-9bd5-05f1-ebbc-0e053afea88d/886449812868.jpg/100x100bb.jpg",
                    "genres": [
                        {
                            "genreId": "18",
                            "name": "Hip-Hop/Rap",
                            "url": "https://itunes.apple.com/us/genre/id18"
                        },
                        {
                            "genreId": "34",
                            "name": "Music",
                            "url": "https://itunes.apple.com/us/genre/id34"
                        }
                    ],
                    "url": "https://music.apple.com/us/album/broadway-girls-feat-morgan-wallen/1600721938?i=1600722156"
                }
            ]

    def test_service_get_json(self):
        """ Test json URL valid.
        """
        data_test_imported = import_json(self.url_song)
        self.assertTrue(isinstance(data_test_imported, dict), "data not valid.")

    def test_service_not_valid_json(self):
        """ Test json with URL not valid.
        """
        url_fake = "http://ssssssssfaken.org"
        data_test_imported = import_json(url_fake)
        self.assertFalse(isinstance(data_test_imported, dict))

    def test_service_import_json_to_dic(self):
        """ Test return service convert the json response to dic python format
        """
        data_dic_test = get_songs()
        self.assertTrue(isinstance(data_dic_test, list), "data is not a list.")

    def test_service_import_top_song(self):
        """ Test return service convert the json response to dic python format
        """
        test_limit = 50
        data_dic_test = get_last_song(test_limit)
        self.assertEqual(len(data_dic_test), test_limit, "list is more larger that limit")

    def test_service_import_genres(self):
        """ Test import genres data
        """
        genders = get_genres_data(self.song_data)
        self.assertTrue(isinstance(genders, list), "data is not a list.")

    def test_service_import_artists(self):
        """ Test import artist data
        """
        artists = get_artist_data(self.song_data)
        self.assertTrue(isinstance(artists, list), "data is not a list.")

    def test_service_import_songs(self):
        """ Test import songs data
        """
        songs = get_songs_data(self.song_data)
        self.assertTrue(isinstance(songs, list), "data is not a list.")
