"""Handles interactions with discord.
"""

import discord
from discord.ext import commands

_bot = discord.Bot()
_guild_ids = [845735383173169212]

@_bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(_bot))

@_bot.slash_command(guild_ids = _guild_ids,
                    name = "greetings",
                    description = "Say hi to the bot!")
async def greetings(ctx):
    await ctx.respond('Hello!')

def start_bot(bot_token, guild_ids):
    _guild_ids = guild_ids
    _bot.run(bot_token)

"""
class GameManager(commands.Cog):
    The class that handles managing the games, such as adding or
    deleting sessions. Does *not* handle user interactions with the
    games themselves.

    def __init__(self, bot):
        # TODO: See if this is neccesary
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
        print('We have logged in as {0.user}'.format(_client))

    @commands.slash_command()
    async def say_hello(message):
        if message.author == _client.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
"""