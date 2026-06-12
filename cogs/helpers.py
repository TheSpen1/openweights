from google import genai
import discord
from discord.ext import commands
import os

log_channel = 1514895510639743027

client = genai.Client(api_key=os.getenv("GOOGLE_LLM_API"))

async def ask(prompt: str) -> str:
    response = await client.aio.models.generate_content(
        model="gemma-4-31b-it",
        contents=prompt
    )
    return response.text

async def permerror(permission: str) -> discord.Embed:
    embed = discord.Embed(
        title="Missing Permission",
        description=f"You need the **{permission}** permission to use this command.",
        color=discord.Color.red()
    )
    return await embed

