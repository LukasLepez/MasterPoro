""" Regroup all MasterPoro commands """

import random
import json

from discord.ext.commands import Bot
from modules import guilds_language as guildsLanguage


with open('config.json', 'r') as config:
    config = json.load(config)


BOT = Bot(command_prefix='$')


@BOT.command()
async def hello(ctx):
    """ Command to say hello """
    id_guilds = str(BOT.guilds[0].id)
    language_module = guildsLanguage.check_guilds_language(id_guilds)
    await ctx.send(language_module.hello_message)


@BOT.command()
async def lang(ctx, arg: str):
    """ Command to change language of discord server """
    id_guilds = str(BOT.guilds[0].id)

    guildsLanguage.check_guilds_language(id_guilds)

    result = guildsLanguage.change_guilds_language(arg, id_guilds)

    await ctx.send(result)


@BOT.command()
async def poke(ctx):
    """ Command to randomly mention a member of the discord """
    list_member = list(filter(
        lambda member: member.bot is not True and member != ctx.author, BOT.guilds[0].members
    ))
    member = random.choice(list_member)
    await ctx.send(member.mention)


@BOT.command()
async def join(ctx):
    """ Command to add discord bot to the current channel """
    channel = ctx.author.voice.channel
    await channel.connect()


@BOT.command()
async def leave(ctx):
    """ Command to leave discord bot to the current channel """
    await ctx.voice_client.disconnect()


BOT.run(config['token'])
