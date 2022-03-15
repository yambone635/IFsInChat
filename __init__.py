"""Entry point for the bot client.
"""

import os

from dotenv import load_dotenv

import discord_interface as di

load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]
TEST_SERVER_GID = [int(os.environ["TEST_SERVER_GID"])]

di.start_bot(BOT_TOKEN)#, TEST_SERVER_GID)
