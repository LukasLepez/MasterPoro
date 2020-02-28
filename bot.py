""" Regroup all MasterPoro commands """

import os
import sys
import random
import nacl

from dotenv import load_dotenv
from discord.ext import commands as botCommands
from functions import guilds_language

sys.path.append('lang')
load_dotenv()

# Creation of different variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Configure the bot so that commands is prefix "$"
BOT = botCommands.Bot(command_prefix='$')


# Function to say hello
@BOT.command()
async def hello(ctx):
    """ Command to say hello """
    id_guilds = str(BOT.guilds[0].id)
    language_module = guilds_language.check_guilds_language(id_guilds)
    await ctx.send(language_module.hello_message)


# Function that changes the language of server
@BOT.command()
async def lang(ctx, arg: str):
    """ Command to change language of discord server """
    id_guilds = str(BOT.guilds[0].id)

    guilds_language.check_guilds_language(id_guilds)

    result = guilds_language.change_guilds_language(arg, id_guilds)

    await ctx.send(result)


@BOT.command()
async def poke(ctx):
    """ Command to randomly mention a member of the discord """
    list_member = list(filter(
        lambda member: member.bot is not True and member != ctx.author, BOT.guilds[0].members
    ))
    member = random.choice(list_member)
    await ctx.send(member.mention)


# @BOT.command()
# async def join(ctx):
#     channel = ctx.author.voice.channel
#     print(ctx.author.voice)
#     await channel.connect()


# @BOT.command()
# async def leave(ctx):
#     await ctx.bot.voice_clients.disconnect()

BOT.run(TOKEN)
