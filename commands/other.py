import random

from discord.ext import commands as Commands
from modules.lang import guilds_language as guildsLanguage

class Other(Commands.Cog):
    """ Regroup all other commands """
    @Commands.command(description='Say hello')
    async def hello(self, ctx):
        """ Say hello """
        id_guilds = str(ctx.guild.id)
        language_module = guildsLanguage.check_guilds_language(id_guilds)
        await ctx.send(language_module.HELLO_MESSAGE)


    @Commands.command(description='Randomly mention a member of the discord ')
    async def poke(self, ctx):
        """ Randomly mention a member of the discord """
        list_member = list(filter(
            lambda member: member.bot is not True and member != ctx.author, ctx.guild.members
        ))
        member = random.choice(list_member)

        await ctx.send(member.mention)
