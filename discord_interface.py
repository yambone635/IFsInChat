"""Handles interactions with discord.
"""

import disnake
import os

from disnake.ext import commands
from dotenv import load_dotenv

import if_interface as ifi

load_dotenv()
TEST_SERVER_GID = [int(os.environ["TEST_SERVER_GID"])]

bot = commands.Bot()

@bot.event
async def on_ready():
    print('Logged in as {0.user}.'.format(bot))

class GameInstance(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.interpreter = ifi.Interpreter()
        self.interpreter.get_output() # Clear the buffer

    @commands.slash_command(name = "c",
        description = "Sends a command to the currently running game.",
        guild_ids = TEST_SERVER_GID)
    async def test(self,
                   inter: disnake.ApplicationCommandInteraction,
                   if_command):
        """Sends a command to the currently running game."""
        self.interpreter.send_command(if_command)
        response = self.interpreter.get_output()
        await inter.response.send_message(response)

def start_bot(bot_token):
    bot.add_cog(GameInstance(bot))
    bot.run(bot_token)
