"""Entry point for the bot client.
"""

import sys
from threading import Thread

import discord_interface as di

bot_token = ""
guild_ids = []

if (len(sys.argv) > 1):
    bot_token = sys.argv[1].strip()
else:
    bot_token = input("Enter the bot's token here: ").strip()
    print("Thanks! (For future reference, the token can be passed as "
          "the command line argument to skip this prompt.)")
    
if (len(sys.argv) > 2):
    for raw_id in sys.argv[2:]:
        id = int(raw_id.strip())
        guild_ids.append(id)
else:
    raw_id = input("Enter a guild ID here: ")
    guild_ids.append(int(raw_id).strip())
    print("Thanks! (For future reference, the guild IDs can be passed "
          "as command line arguments after the bot token to skip this "
          "prompt and/or provide multiple IDs.)")

print(guild_ids)

di.start_bot(bot_token, guild_ids)

"""
bot_thread = Thread(target = di.start_bot,
                    args = [bot_token, guild_ids])

# Make sure the thread doesn't prevent us from exiting the program
bot_thread.daemon = True

bot_thread.start()

while True:
    command = input().strip()
    if (command == "quit"):
        break
"""
"""
interpreter = ifi.Interpreter()

interpreter.send_command("test")

interpreter.close()

print(interpreter.get_output())
"""
