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
            response = await ask(message)
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(LLM(bot))

#print(chatsee("yo"))