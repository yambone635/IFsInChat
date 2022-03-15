"""Entry point for the bot client.
"""

import os

from dotenv import load_dotenv

import discord_interface as di

load_dotenv()
BOT_TOKEN = os.environ["BOT_TOKEN"]

di.start_bot(BOT_TOKEN)
