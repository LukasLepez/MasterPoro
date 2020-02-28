import os
import sys
import discord

from dotenv import load_dotenv
from discord.ext import commands as botCommands
from functions import guildsLanguage

sys.path.append('lang')
load_dotenv()

# Creation of different variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Configure the bot so that commands is prefix "$"
BOT = botCommands.Bot(command_prefix='$')


# Function to say hello
@BOT.command()
async def hello(ctx):
    id_guilds = str(BOT.guilds[0].id)
    language_module = guildsLanguage.check_guilds_language(id_guilds)
    await ctx.send(language_module.hello_message)


# Function that changes the language of server
@BOT.command()
async def lang(ctx, arg):
    id_guilds = str(BOT.guilds[0].id)

    guildsLanguage.check_guilds_language(id_guilds)

    result = guildsLanguage.change_guilds_language(arg, id_guilds)

    await ctx.send(result)

BOT.run(TOKEN)
