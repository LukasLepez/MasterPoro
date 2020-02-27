import os
import sys
import discord

from os.path import dirname
from dotenv import load_dotenv
from discord.ext import commands as botCommands
from functions import guildsLanguage

sys.path.append('lang')
load_dotenv()

# Creation of different variables
TOKEN = os.getenv('DISCORD_TOKEN')

languageModule = ''

# Configure the bot so that commands is prefix "$"
bot = botCommands.Bot(command_prefix='$')


# Function to say hello
@bot.command()
async def hello(ctx):
    languageModule = guildsLanguage.check_guilds_language(idGuilds)
    await ctx.send(languageModule.hello_message)


# Function that changes the language of server
@bot.command()
async def lang(ctx, arg):
    idGuilds = str(bot.guilds[0].id)

    languageModule = guildsLanguage.check_guilds_language(idGuilds)

    result = guildsLanguage.change_guilds_language(arg, idGuilds)

    await ctx.send(result)

bot.run(TOKEN)
