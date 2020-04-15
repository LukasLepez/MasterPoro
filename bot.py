""" 
Main file used to launch the bot
"""

import json

from commands.language import Language
from commands.voice import Voice
from commands.dice import Dice

import discord
from discord.ext import commands as Commands



with open('config.json', 'r') as config:
    CONFIG = json.load(config)


BOT = Commands.Bot(command_prefix='$')
BOT.remove_command('help')


@BOT.event
async def on_ready():
    """ Configure the bot when it is operational """
    activity = discord.Game(name="$help")
    await BOT.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")


BOT.add_cog(Language(BOT))
BOT.add_cog(Voice(BOT))
BOT.add_cog(Dice(BOT))

LANGUAGE = BOT.get_cog('Language').get_commands()
VOICE = BOT.get_cog('Voice').get_commands()
DICE = BOT.get_cog('Dice').get_commands()

LIST_COMMANDS = [LANGUAGE, VOICE, DICE]
COMMANDS = []

for items in LIST_COMMANDS:
    for item in items:
        item.name = f'${item.name}'
        COMMANDS.append(item)


@BOT.command()
async def help(ctx):
    """ List all commands """
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name='List of commands')
    for command in COMMANDS:
        embed.add_field(name=command.name, value=command.description, inline=False)

    await ctx.send(embed=embed)


BOT.run(CONFIG['token'])
