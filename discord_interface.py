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
        self.interpreter = None
        self.running_game = False
    
    @commands.slash_command(name = "start_game",
        description = "Starts a new game.",
        guild_ids = TEST_SERVER_GID)
    async def start_game(self,
                   inter: disnake.ApplicationCommandInteraction):
        """Initializes the interpreter with a new game."""

        if (self.interpreter is not None):
            self.interpreter.close()

        self.interpreter = ifi.Interpreter(game_filename = "zork1.z3")
        response = self.interpreter.get_output()
        await inter.response.send_message(response)
        self.running_game = True

    @commands.slash_command(
        name = "c",
        description = "Sends a command to the currently running game.",
        guild_ids = TEST_SERVER_GID)
    async def send_if_command(
            self,
            inter: disnake.ApplicationCommandInteraction,
            if_command):
        """Sends a command to the currently running game."""
        if (self.running_game):
            if not if_command:
                if_command = ""
            
            print("Recieved command: " + if_command)
            
            self.interpreter.send_command(if_command.strip())
            response = self.interpreter.get_output()

            await inter.response.send_message(response)
        else:
            await inter.response.send_message(
                "You need to start a game first!"
            )

def start_bot(bot_token):
    bot.add_cog(GameInstance(bot))
    bot.run(bot_token)
