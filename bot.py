""" Regroup all MasterPoro commands """

import random
import json
import discord

from discord.ext import commands
from modules.lang import guilds_language as guildsLanguage


with open('config.json', 'r') as config:
    CONFIG = json.load(config)


class Language(commands.Cog):
    """ Regroup all language commands """
    @commands.command(description='Change language of discord server')
    async def lang(self, ctx, arg: str):
        """ Change language of discord server """
        id_guilds = str(BOT.guilds[0].id)

        guildsLanguage.check_guilds_language(id_guilds)

        result = guildsLanguage.change_guilds_language(arg, id_guilds)

        await ctx.send(result)


class Voice(commands.Cog):
    """ Regroup all voice commands """
    @commands.command(description='Add discord bot to the current channel')
    async def join(self, ctx):
        """ Add discord bot to the current channel """
        channel = ctx.author.voice.channel
        await channel.connect()


    @commands.command(description='Leave discord bot to the current channel')
    async def leave(self, ctx):
        """ Leave discord bot to the current channel """
        await ctx.voice_client.disconnect()


class Other(commands.Cog):
    """ Regroup all other commands """
    @commands.command(description='Say hello')
    async def hello(self, ctx):
        """ Say hello """
        id_guilds = str(BOT.guilds[0].id)
        language_module = guildsLanguage.check_guilds_language(id_guilds)
        await ctx.send(language_module.HELLO_MESSAGE)


    @commands.command(description='Randomly mention a member of the discord ')
    async def poke(self, ctx):
        """ Randomly mention a member of the discord """
        list_member = list(filter(
            lambda member: member.bot is not True and member != ctx.author, BOT.guilds[0].members
        ))
        member = random.choice(list_member)
        await ctx.send(member.mention)


BOT = commands.Bot(command_prefix='$')
BOT.remove_command('help')


@BOT.event
async def on_ready():
    """ Configure the bot when it is operational """
    activity = discord.Game(name="$help for command")
    await BOT.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print("Bot is ready!")


# CODE A OPTIMISER
BOT.add_cog(Language(BOT))
BOT.add_cog(Voice(BOT))
BOT.add_cog(Other(BOT))

LANGUAGE = BOT.get_cog('Language').get_commands()
VOICE = BOT.get_cog('Voice').get_commands()
OTHER = BOT.get_cog('Other').get_commands()

LIST_COMMANDS = [LANGUAGE, VOICE, OTHER]
COMMANDS = []

for items in LIST_COMMANDS:
    for item in items:
        item.name = f'${item.name}'
        COMMANDS.append(item)


@BOT.command()
async def help(ctx):
    """ List all commands """
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name='List of commands')
    for command in COMMANDS:
        embed.add_field(name=command.name, value=command.description, inline=False)

    await ctx.send(author, embed=embed)


BOT.run(CONFIG['token'])
