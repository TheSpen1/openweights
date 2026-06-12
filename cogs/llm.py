import discord
from discord.ext import commands
from cogs.helpers import ask

async def chatsee(prompt):
    return await ask(prompt)

class LLM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, ctx, *, message: str):
        async with ctx.typing():
            try:
                response = await ask(message)
                if not response:
                    await ctx.send("Got an empty response.")
                    return
                await ctx.send(response)
            except Exception as e:
                await ctx.send(f"Error: {e}")

async def setup(bot):
    await bot.add_cog(LLM(bot))
