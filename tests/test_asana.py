import base64
import unittest
import six

from asana import asana

class TestAsana(unittest.TestCase):
    dummy_key = "dummy_key"
    asana_api = asana.AsanaAPI(dummy_key, debug=True)

    def test_asana_api_init(self):
        assert self.asana_api.apikey is not None

    def test_get_basic_auth_returns_base64_encode(self):
        encoded_key = self.asana_api.get_basic_auth()

        decoded_key = base64.b64decode(encoded_key)
        assert decoded_key == six.b(self.dummy_key + ":")
