from json import JSONDecoder
import discord
import osuExchange

osu_client = osuExchange.OsuApiClient(**JSONDecoder().decode(open('client-info.json').read()))

TESTING_GUILD = discord.Object(id=1131342149301055488)

class OsuExchangeBot(discord.Client):
	def __init__(self):
		super().__init__(intents=discord.Intents.none())
		self.tree = discord.app_commands.CommandTree(self)
	
	async def setup_hook(self):
		await self.tree.sync(guild=TESTING_GUILD)

client = OsuExchangeBot()

@client.event
async def on_ready():
	assert client.user
	print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.tree.command(guild=TESTING_GUILD)
async def get_user(interaction: discord.Interaction, id: int | str):
	"""Get info about an osu! player."""
	user = osu_client.users.get(id)
	assert user.rank_highest
	embed = discord.Embed(title=user.username)
	embed.set_author(name='osu! player info')
	embed.set_thumbnail(url=user.avatar_url)
	embed.add_field(name='Peak Rank', value=f'''#{f'{user.rank_highest.rank:,}'} {user.rank_highest.updated_at.date()}''')
	if user.beatmap_playcounts_count:
		embed.add_field(name='Total Beatmaps Played', value=user.beatmap_playcounts_count)
	await interaction.response.send_message(embed=embed)

client.run(open('discord-bot-token').read())
