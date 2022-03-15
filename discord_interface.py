"""Handles interactions with discord.
"""

import disnake
import os

from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()
TEST_SERVER_GID = [int(os.environ["TEST_SERVER_GID"])]

bot = commands.Bot()

@bot.event
async def on_ready():
    print('Logged in as {0.user}.'.format(bot))

@bot.slash_command(guild_ids = TEST_SERVER_GID)
async def test(inter):
    """Simple test of slash commands."""
    await inter.response.send_message("Hello!")

def start_bot(bot_token):
    bot.run(bot_token)
