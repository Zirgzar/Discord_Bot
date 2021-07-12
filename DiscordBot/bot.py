import os
import discord
from dotenv import load_dotenv

load_dotenv()
# Loads bot token and server
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    # Prints server(s) that bot is part of
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

    # Welcomes bot to server
    print(f'{client.user}, welcome to the Scrub Box!')

    # Prints member list
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


client.run(TOKEN)