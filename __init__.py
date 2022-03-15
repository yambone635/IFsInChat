"""Entry point for the bot client.
"""

import if_interface as ifi
import discord_interface as di

import sys

bot_token = ""

if (len(sys.argv) > 1):
    bot_token = sys.argv[1].strip()
if (not bot_token):
    bot_token = input ("Enter the bot's token here: ").strip()
    print("Thanks! (For future reference, the token can be passed as "
          + "the command line argument to skip this prompt.)")

bot_client = di.start_client(bot_token)

"""
interpreter = ifi.Interpreter()

interpreter.send_command("test")

interpreter.close()

print(interpreter.get_output())
"""
