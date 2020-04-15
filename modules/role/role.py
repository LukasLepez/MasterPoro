"""
Allows you to manage the roles of a server discord (guilds)
"""

def check_role(role_member, id_guilds: str):
    """ Function that checks the role of the member """
    role = []

    for item in role_member:
        role.append(item.name)

    result = list(filter(lambda x: x == ["Créateur", "Maitre de jeu"], role))

    if result:
        return True
    else:
        return False
