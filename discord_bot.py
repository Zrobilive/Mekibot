import discord
from discord.ext import commands
import time
import datetime
from keepalive import keep_alive
from PIL import Image, ImageFilter
from io import BytesIO



intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)


@client.event
async def on_ready():
  guild = client.get_guild(823577971688341554)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(guild.members)} tag! | Parancokért: !help"))
  print("Készen vagyok, mehetünk!")


  token = 'ODI3ODc1Njk0NTUzNDY0ODQy.YGhZUg.-gme-I5hpmEowBF6dmf1amsRQSw'

  @client.command()
  async def ping(ctx):
      await ctx.send(f'PONG! Amúgy ekkora a késésem: {round(client.latency * 1000)}ms')

  @client.command()
  async def pong(ctx):
      await ctx.send('Ez visszafele nem működik, hehe!')

  @client.command()
  async def takarítás(ctx, amount=5):
      await ctx.channel.purge(limit=amount)



@client.command()
async def egetes(ctx, member:discord.Member=None):
  if not member:
    member = ctx.author

  rip = Image.open('egetes.jpg')
  asset= member.avatar_url_as(size=128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((168,178))


  rip.paste(pfp, (60,93))

  rip.save('pegetes.jpg')

  await ctx.send(file = discord.File('pegetes.jpg'))






keep_alive()
client.run(token)