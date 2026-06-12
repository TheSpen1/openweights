import asyncio
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    # Auto-load all the cogs 
    for filename in os.listdir("./cogs") :
        if filename.endswith(".py") and filename not in ("__init__.py","fun.py","moderation.py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
    print("BOT IS LIVE!")
    await bot.start(os.getenv("DISCORD_TOKEN"))
    

asyncio.run(main())