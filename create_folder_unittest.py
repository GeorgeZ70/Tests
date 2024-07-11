import unittest
import requests

class TestCreateFolder(unittest.TestCase):
    def setUp(self):
        self.headers = {
            'Authorization': 'OAuth ...'
        }
    def test_create_folder(self) :
            for i, (key, value, expected) in enumerate([
            ('pathe', 'Photo', 400),
            ('path', 'Photo', 201),
            ('path', 'Photo', 409)
            ]):  
                params = {key: value}                         
                with self.subTest(i):
                    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                            headers = self.headers, params = params)
                    result = response.status_code
                    self.assertEqual(expected, result)
    def tearDown(self):
        params = {'path': 'Photo'}
        requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                        headers = self.headers, params = params)        
            