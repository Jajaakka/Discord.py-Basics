import discord
import os
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="?")

keep_alive()
bot.run(os.getenv('TOKEN'))
