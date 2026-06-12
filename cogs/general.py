import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} joined")

async def setup(bot):
    await bot.add_cog(General(bot))