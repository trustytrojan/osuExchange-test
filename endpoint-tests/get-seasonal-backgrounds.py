from osuExchange import OsuApiClient
from json import JSONDecoder

client = OsuApiClient(**JSONDecoder().decode(open('client-info.json').read()))

user_id = 8908337
beatmap_id = 939209

print(f'Fetching scores for user with id {user_id} on beatmap {beatmap_id}')

bgs = client.get_seasonal_backgrounds()

for bg in bgs.backgrounds:
    print(bg.url)

#print(f"A link to a Seasonal Background: {bgs.backgrounds[1].url}")
