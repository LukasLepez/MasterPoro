"""
Regroup all MasterPoro voice commands 
"""

from discord.ext import commands as Commands

class Voice(Commands.Cog):
    """ Regroup all voice commands """
    @Commands.command(description='Add discord bot to the current channel')
    async def join(self, ctx):
        """ Add discord bot to the current channel """
        channel = ctx.author.voice.channel
        await channel.connect()


    @Commands.command(description='Leave discord bot to the current channel')
    async def leave(self, ctx):
        """ Leave discord bot to the current channel """
        await ctx.voice_client.disconnect()
