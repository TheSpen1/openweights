import discord
from discord.ext import commands
from cogs.helpers import *

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if log_channels[member.guild]:
            channel = self.bot.get_channel(log_channel)  # integer, no quotes
            embed = discord.Embed(
                title="Member Join",
                description=f"""
                    Global Name: {member.global_name}
                    ID: {member.id}""",
                color=0x5865F2
            )
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Events(bot))