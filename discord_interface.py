"""Handles interactions with discord.
"""

import discord

_client = discord.Client()

def start_client(bot_token):
    _client.run(bot_token)

@_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(_client))

@_client.event
async def on_message(message):
    if message.author == _client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
