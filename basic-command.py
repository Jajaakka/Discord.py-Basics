import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="?")

@bot.command()
async def hi(ctx):
  await ctx.send('hello.')

keep_alive()
bot.run(os.getenv('TOKEN'))
