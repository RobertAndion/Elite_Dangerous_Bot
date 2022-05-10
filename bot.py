import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()

client = commands.Bot(command_prefix='>',intents=intents)

@client.event
async def on_ready():
    print("Bot is live")
    #client.load_extension('playlist')
    #for file in os.listdir("./Cogs"):
    #    if file.endswith(".py"):
    #        client.load_extension(f'Cogs.{file[:-3]}')

client.run(DISCORD_TOKEN)