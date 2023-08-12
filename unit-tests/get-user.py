from osuExchange import OsuApiClient
from unittest import TestCase, main

class GetUserTest(TestCase):
	def setUp(self):
		self.client = OsuApiClient.from_json_file('client-info.json')

	def test1ById(self):
		user = self.client.users.get(12625512)
		self.assertEqual(user.id, 12625512)
		self.assertEqual(user.username, 'TrustyTrojan')
		self.assertEqual(user.country_code, 'US')
		self.assertFalse(user.is_deleted)
		self.assertFalse(user.is_bot)
		self.assertFalse(user.has_supported)
		self.assertFalse(user.is_supporter)
		self.assertIsNone(user.discord)
		self.assertIsNone(user.twitter)
		self.assertIsNone(user.website)

	def test1ByUsername(self):
		user = self.client.users.get('TrustyTrojan')
		self.assertEqual(user.id, 12625512)
		self.assertEqual(user.username, 'TrustyTrojan')
		self.assertEqual(user.country_code, 'US')
		self.assertFalse(user.is_deleted)
		self.assertFalse(user.is_bot)
		self.assertFalse(user.has_supported)
		self.assertFalse(user.is_supporter)
		self.assertIsNone(user.discord)
		self.assertIsNone(user.twitter)
		self.assertIsNone(user.website)

	# write more tests for other users

if __name__ == '__main__':
	main()
