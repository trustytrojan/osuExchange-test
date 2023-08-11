from osuExchange import OsuApiClient
from unittest import TestCase
from json import JSONDecoder

client_info = JSONDecoder().decode(open('client-info.json').read())

class OsuApiClientTest(TestCase):
	def setUp(self):
		self.client = OsuApiClient(**client_info)
	
	def test_get_user_1(self):
		user = self.client.get_user(10652591)
		self.assertEqual(user.username, 'a sushi roll')
		