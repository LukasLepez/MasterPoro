"""
Regroup all Adventure Man language commands 
"""

from discord.ext import commands
from modules.lang import guilds_language as guildsLanguage
from modules.role import role

class Language(commands.Cog):
    """ Regroup all language commands """
    @commands.command(description='Change language of discord server')
    async def lang(self, ctx, arg: str):
        role_member = ctx.message.author.roles
        id_guilds = str(ctx.guild.id)

        if role.check_role(role_member, id_guilds) is True:
            result = guildsLanguage.change_guilds_language(arg, id_guilds)
        else:
            language_module = guildsLanguage.check_guilds_language(id_guilds)
            result = language_module.NO_PERMISSION

        await ctx.send(result)
