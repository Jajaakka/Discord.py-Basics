import discord
import os
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='?')

@bot.command()
async def hi(ctx):
  em = discord.Embed(title="Hello!",color=discord.Color.teal()) 
  await ctx.send(embed=em)
  
  keep_alive()
  bot.run(os.getenv('TOKEN'))
