from osuExchange import OsuApiClient

client = OsuApiClient.from_json_file('client-info.json')

user_id = 10652591

print(f'Fetching user with id {user_id} for mode "osu"')

user = client.users.get(user_id, mode='osu')

print('Fetched user! Now printing a few details:\n')

print(f'User name: {user.username}')
print(f'User join date: {user.join_date}')
print(f'User country code: {user.country_code}')
print(f'Is user online now? {"Yes" if user.is_online else "No"}')
