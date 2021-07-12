import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
# Loads bot token and server
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

"""
Need to find how to get intents working whil implementing class

class ScrubClient(discord.Client):
    async def on_ready(self):
        discord.Intents.all()
        discord.Client(intents=intents)
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(f'{self.user}, welcome to the Scrub Box!')

        # Prints member list
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')
        # Prints server(s) that bot is part of
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name} (id: {guild.id})'
        )

"""

"""
Implement as bot commands at a later time

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
"""


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f"{client.user.name} has connected to Discord.")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome, {member.name}, to the Scrub Box!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    soulliners = [
        "Git gud, scrub!",
        "What rings you got, bithc?",
        "We are born of the blood, made men by the blood, undone by the blood. Our eyes are yet to open... Fear the old blood.",
        "Bear, seek, seek, lest.",
        "Umbasa.",
    ]
    tryingtoforce = "STFU biiiiiiitch!"

    if "help" in message.content.lower():
        response = random.choice(soulliners)
        await message.channel.send(response)
    # elif message.content == "raise-exception":
    # raise discord.DiscordException

    if "raise-exception" in message.content.lower():
        await message.channel.send(tryingtoforce)

    if "!random" in message.content.lower():
        randroll = f"{message.author} rolled {random.randint(1, 99)}!"
        await message.channel.send(randroll)


"""
Raise error

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
"""


# client = ScrubClient()
client.run(TOKEN)
