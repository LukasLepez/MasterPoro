from discord.ext import commands
from modules.lang import guilds_language as guildsLanguage

class Language(commands.Cog):
    """ Regroup all language commands """
    @commands.command(description='Change language of discord server')
    async def lang(self, ctx, arg: str):
        """ Change language of discord server """
        id_guilds = str(ctx.guild.id)

        guildsLanguage.check_guilds_language(id_guilds)

        result = guildsLanguage.change_guilds_language(arg, id_guilds)

        await ctx.send(result)
