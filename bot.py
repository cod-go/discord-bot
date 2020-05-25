import os

import discord
from dotenv import load_dotenv
import random

from messages import BROKLYN_99_QUOTES

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    guild = None
    for g in client.guilds:
        if g.name == GUILD:
            guild = g

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '99!':
        response = random.choice(BROKLYN_99_QUOTES)
        await message.channel.send(response)

client.run(TOKEN)
