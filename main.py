import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
import random
import time, datetime
import requests
import json
import asyncio

# Logging setup
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Intents setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix='$', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    global startTime
    startTime = time.time()

# Event: Member join
@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)

# Event: On message (ensure commands are processed)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    # Process commands
    await bot.process_commands(message)

bot.remove_command('help') 

async def load_cogs():
    for folder in os.listdir("./commands"):
        folder_path = f"./commands/{folder}"
        if os.path.isdir(folder_path) and folder != "__pycache__":
            for filename in os.listdir(folder_path):
                if filename.endswith(".py"):
                    cog_path = f"commands.{folder}.{filename[:-3]}"
                    try:
                        await bot.load_extension(cog_path)
                    except Exception as e:
                        print(f"Failed to load cog {cog_path}: {e}")

# Main entry point for the bot
async def main():
    async with bot:
        await load_cogs()  # Load all cogs from the cogs folder
        await bot.start(BOT_TOKEN)

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())