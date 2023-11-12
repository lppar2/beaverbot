import os
import random
import discord
from discord.ext import commands

TOKEN = 'TOKEN'
intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)
trigger = ['бобр', 'бобер', 'бобёр']


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
    print(message.content)
    if any(word in message.content.lower() for word in trigger):
        image_folder = 'beaver'
        image_files = os.listdir(image_folder)
        random_image = random.choice(image_files)
        image_path = os.path.join(image_folder, random_image)
        if not bot.user == message.author:
            await message.channel.send(file=discord.File(image_path))
    await bot.process_commands(message)


bot.run(TOKEN)
