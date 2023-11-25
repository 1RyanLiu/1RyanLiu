import discord
from discord import File
from discord.ext import commands
from discord import Interaction
from keep_alive import keep_alive
import math 
import os
import random

intents = discord.Intents.all()


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!command"))
    print('Bot is ready')

@bot.command(name='ping', description='Ping pong command')
async def ping(ctx):
    if bot.latency * 1000 > 0:
        await ctx.send(f'Pong! {(bot.latency * 1000)}ms')
    else:
        await ctx.send('You beat me!!')

@bot.command(name='hello', description='Hello command')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='join', description='Join a voice channel')
async def join(ctx):
    voice_channel = ctx.voice_client
    if voice_channel:
        try:
            await voice_channel.connect()
        except discord.ClientException as e:
            await ctx.send(f'Error: {e}')
    else:
        await ctx.send('You are not in a voice channel!')

@bot.command(name='leave', description='Leave the voice channel')
async def leave(ctx):
    voice_channel = ctx.voice_client
    if voice_channel:
        try:
            await voice_channel.disconnect()
            await ctx.send('Disconnected')
        except discord.ClientException as e:
            await ctx.send(f'Error: {e}')
    else:
        await ctx.send('I am not currently in a voice channel.')

@bot.command(help='Displays available commands')
async def command(ctx):
    embed = discord.Embed(
        title='Available Commands',
        description='Here is a list of available commands:',
        color=discord.Color.blue()  # You can change the color to your preference
    )

    embed.add_field(name='!hello', value='Say hello!', inline=False)
    embed.add_field(name='!ping', value='Check the bot\'s latency.', inline=False)
    embed.add_field(name='!meme', value='Display a random meme.', inline=False)
    embed.add_field(name='!plus', value='Addition operation.', inline=False)
    embed.add_field(name='!minus', value='Subtraction operation.', inline=False)
    embed.add_field(name='!multiply', value='Multiplication operation.', inline=False)
    embed.add_field(name='!divide', value='Division operation.', inline=False)
    embed.add_field(name='!sin', value='Sine operation.', inline=False)
    embed.add_field(name='!cos', value='Cosine operation.', inline=False)
    embed.add_field(name='!tan', value='Tangent operation.', inline=False)
    embed.add_field(name='!log', value='Logarithm operation.', inline=False)
    embed.add_field(name='!sqrt', value='Square root operation.', inline=False)
    embed.add_field(name='!power', value='Exponential operation.', inline=False)

    await ctx.send(embed=embed)

@bot.command(help='add command')
async def add(ctx, *args):
  total = 0
  for arg in args:
    total += float(arg)
  await ctx.send(total)

@bot.command(help='minus')
async def minus(ctx, *args):
  total = float(args[0])

  for arg in range(1, len(args)):
    total -= float(args[arg])
  
  await ctx.send(total)

@bot.command(help='multiply command')
async def multiply(ctx, *args):

  total = float(args[0])

  for arg in range(1, len(args)):
      total *= float(args[arg])

  await ctx.send(total)

@bot.command(help='divide command')
async def divide(ctx, var1, var2):
  await ctx.send(float(var1) / float(var2))

@bot.command(help='sqrt command')
async def sqrt(ctx, var1):
  await ctx.send(math.sqrt(float(var1)))

@bot.command(help='log command')
async def log(ctx, var1):
  await ctx.send(math.log(float(var1)))

@bot.command(help='sin command')
async def sin(ctx, var1):
  await ctx.send(math.sin(float(var1)))

@bot.command(help='cos command')
async def cos(ctx, var1):
  await ctx.send(math.cos(float(var1)))

@bot.command(help='tan command')
async def tan(ctx, var1):
  await ctx.send(math.tan(float(var1)))

@bot.command(help='power command')
async def power(ctx, var1, var2):
  total = float(var1)
  for i in range(int(var2) - 1):
    total *= float(var1)

  await ctx.send(total)

@bot.command(help='random meme')
async def meme(ctx):
  meme_folder_path = "memes"
  files = os.listdir(meme_folder_path)
  image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
  
  if not image_files:
      await ctx.send("No meme images found.")
  else:
      random_meme = random.choice(image_files)

      meme_path = os.path.join(meme_folder_path, random_meme)
    
      with open(meme_path, 'rb') as file:
          meme_file = File(file)
          await ctx.send(file=meme_file)

keep_alive()
my_secret = os.environ['discord_bot'] 
bot.run(my_secret)
