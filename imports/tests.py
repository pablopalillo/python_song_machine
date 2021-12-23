from django.test import TestCase
from .services import import_json, get_songs, get_last_song


class TestServicesImport(TestCase):

    url_song = "https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json"

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
        self.assertTrue(isinstance(data_dic_test, list), "data is not a dict.")

    def test_service_import_top_song(self):
        """ Test return service convert the json response to dic python format
        """
        test_limit = 50
        data_dic_test = get_last_song(test_limit)
        self.assertEqual(len(data_dic_test), test_limit, "list is more larger that limit")

    def test_service_import_genres(self):
        """ Test import genres data
        """
        pass

    def test_service_import_artists(self):
        """ Test import artist data
        """
        pass

    def test_service_import_songs(self):
        """ Test import songs data
        """
        pass
