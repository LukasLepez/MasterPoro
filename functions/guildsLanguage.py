import json
import importlib

# Function that checks the language of servers (guilds)
def check_guilds_language(id_guilds):
    with open('./lang/server.json', 'r') as jsonFileRead:
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

        with open("./lang/server.json", "w") as jsonFileWrite:
            json.dump(data, jsonFileWrite)
        
        jsonFileWrite.close()
        
        lang_guilds = 'en'
    else:
        lang_guilds = lang_json_r[id_guilds]['language']

    global languageModule
    languageModule = __import__(lang_guilds)

    jsonFileRead.close()

    return languageModule



def change_guilds_language(arg, idGuilds):
    if arg == "fr" or arg == "en":
        with open('lang/server.json', 'r') as jsonFileRead:
            lang_json_r = json.load(jsonFileRead)
        
        lang_json_r[idGuilds]['language'] = arg

        with open('lang/server.json', 'w') as jsonFileWrite:
            json.dump(lang_json_r, jsonFileWrite)

        jsonFileRead.close()
        jsonFileWrite.close()

        languageModule = check_guilds_language(idGuilds)

        importlib.reload(languageModule)

        return languageModule.success_language_message

    else:
        # Return an error message because the variable "arg" has an incorrect value
        return languageModule.error_language_message