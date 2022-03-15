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
    
    @commands.slash_command(name = "list_games",
        description = "Lists the available games.",
        guild_ids = TEST_SERVER_GID)
    async def list_games(self,
                   inter: disnake.ApplicationCommandInteraction):
        """Lists the available games."""
        game_files = os.listdir("./games/")

        game_list_string = "Games available:\n"
        for game_filename in game_files:
            game_name = game_filename.split(".")[0]
            game_list_string += ' - ' + game_name + '\n'
        game_list_string = game_list_string[:-1]

        await inter.response.send_message(game_list_string)
    
    @commands.slash_command(name = "start_game",
        description = "Starts a new game.",
        guild_ids = TEST_SERVER_GID)
    async def start_game(self,
                   inter: disnake.ApplicationCommandInteraction,
                   game_name):
        """Initializes the interpreter with a new game."""
        game_files = os.listdir("./games/")
        for game_candidate in game_files:
            if game_candidate.split(".")[0] == game_name:
                game_filename = game_candidate
                break

        if game_filename is None:
            await inter.response.send_message(
                "No games found with given name"
            )
            return

        if (self.interpreter is not None):
            self.interpreter.close()

        self.interpreter = ifi.Interpreter(game_filename)
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
