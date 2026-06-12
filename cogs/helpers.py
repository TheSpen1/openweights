from google import genai
import discord
from discord.ext import commands
import os

log_channel = 1514895510639743027
system_prompt = f"""
You are Dexel, a Discord bot and general assistant for a community server. 
You're helpful, direct, and have a casual but not overly informal tone — 
think knowledgeable friend, not customer support. Don't over-explain. 
No markdown formatting, no bullet points, no bold text. 
Keep responses under 3-4 sentences unless the question genuinely needs more detail. Keep it under 400 tokens no matter what. 

User message: 
"""

client = genai.Client(api_key=os.getenv("GOOGLE_LLM_API"))

async def ask(prompt: str) -> str:
    response = await client.aio.models.generate_content(
        model="gemma-4-31b-it",
        contents=system_prompt+prompt,
        config=genai.types.GenerateContentConfig(
            max_output_tokens=400,
        )
    )
    return response.text

async def permerror(permission: str) -> discord.Embed:
    embed = discord.Embed(
        title="Missing Permission",
        description=f"You need the **{permission}** permission to use this command.",
        color=discord.Color.red()
    )
    return await embed

