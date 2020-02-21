import os
import sys
import discord
import importlib
import json

from os.path import dirname
from dotenv import load_dotenv
from discord.ext import commands as botCommands


sys.path.append('lang')
load_dotenv()

import language

# Creation of different variables
TOKEN = os.getenv('DISCORD_TOKEN')

languageModule = ''
lang_result = ''

# Configure the bot so that commands is prefix "$"
bot = botCommands.Bot(command_prefix='$')


# Function that checks the language of servers (guilds)
def language_guilds(id_guilds):
    with open('lang/server.json', 'r') as jsonFileRead:
        lang_json_r = json.load(jsonFileRead)

    global lang_result
    lang_result = list(filter(lambda x : x == str(id_guilds), lang_json_r))
    if lang_result == []:
        data = lang_json_r
        new_data = {
            id_guilds: {
                "language": "en"
            },
        }
        data.update(new_data)

        with open("lang/server.json", "w") as jsonFileWrite:
            json.dump(data, jsonFileWrite)
        
        jsonFileWrite.close()
        
        lang_guilds = 'en'
    else:
        lang_guilds = lang_json_r[lang_result[0]]['language']

    global languageModule
    languageModule = __import__(lang_guilds)

    jsonFileRead.close()



# Function to say hello
@bot.command()
async def hello(ctx):
    language_guilds(bot.guilds[0].id)
    await ctx.send(languageModule.hello_message)



# Function that changes the language of server
@bot.command()
async def lang(ctx, arg):
    # Get the server id
    language_guilds(bot.guilds[0].id)

    if arg == "fr" or arg == "en":
        with open('lang/server.json', 'r') as jsonFileRead:
            lang_json_r = json.load(jsonFileRead)
            
        lang_json_r[lang_result[0]]['language'] = arg

        with open('lang/server.json', 'w') as jsonFileWrite:
            json.dump(lang_json_r, jsonFileWrite)

        jsonFileRead.close()
        jsonFileWrite.close()

        language_guilds(bot.guilds[0].id)

        importlib.reload(languageModule)

        await ctx.send(languageModule.success_language_message)

    else:
        # Returns an error message because the variable "arg" has an incorrect value
        await ctx.send(languageModule.error_language_message)

bot.run(TOKEN)
