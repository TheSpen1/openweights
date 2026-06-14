import discord
from discord.ext import commands
from cogs.helpers import *
import asyncio

class LLM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.LLMinstance = LLMHelper()

    @commands.command()
    async def chat(self, ctx, *, message: str):
        async with ctx.typing():
            response = await self.LLMinstance.askllm(message)
            if isinstance(response, discord.Embed):
                embed = response
            else:
                embed = discord.Embed(
                    description=
                    f"""{response}""",
                    color=discord.Color.blurple()
                )
            await ctx.send(embed=embed, reference=ctx.message)
async def setup(bot):
    await bot.add_cog(LLM(bot))
