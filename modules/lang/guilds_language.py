""" Allows you to manage the language of a server discord (guilds) """

import json
import importlib


def check_guilds_language(id_guilds: str):
    """ Function that checks the language of servers (guilds) """
    with open('./lang/server.json', 'r') as json_file_read:
        lang_json_r = json.load(json_file_read)

    lang_result = list(filter(lambda x: x == str(id_guilds), lang_json_r))
    if lang_result == []:
        data = lang_json_r
        new_data = {
            id_guilds: {
                "language": "en"
            },
        }
        data.update(new_data)

        with open("./lang/server.json", "w") as json_file_write:
            json.dump(data, json_file_write)

        json_file_write.close()
        lang_guilds = 'en'

    else:
        lang_guilds = lang_json_r[id_guilds]['language']

    language_module = __import__(f'lang.{lang_guilds}', fromlist=['object'])

    json_file_read.close()

    return language_module



def change_guilds_language(arg, id_guilds: str):
    """ Function that change the language of servers (guilds) """
    if arg in ("fr", "en"):
        with open('lang/server.json', 'r') as json_file_read:
            lang_json_r = json.load(json_file_read)

        lang_json_r[id_guilds]['language'] = arg

        with open('lang/server.json', 'w') as json_file_write:
            json.dump(lang_json_r, json_file_write)

        json_file_read.close()
        json_file_write.close()

        language_module = check_guilds_language(id_guilds)

        importlib.reload(language_module)

        return language_module.success_language_message

    language_module = check_guilds_language(id_guilds)
    return language_module.error_language_message
