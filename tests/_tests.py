PERMS_DICT: dict = {
    1 << 1: "KICK_MEMBERS",
    1 << 2: "BAN_MEMBERS",
    1 << 3: "ADMIN",
    1 << 4: "MANAGE_CHANNELS",
    1 << 5: "MANAGE_GUILD",
    1 << 7: "AUDIT_LOG",
    1 << 17: "@EVERYONE",
    1 << 22: "MUTE_MEMBERS",
    1 << 23: "DEAFEN_MEMBERS",
    1 << 24: "MOVE_MEMBERS",
    1 << 27: "MANAGE_NICKNAMES",
    1 << 28: "MANAGE_ROLES",
    1 << 30: "MANAGE_EMOJIS_AND_STICKERS",
    1 << 33: "MANAGE_EVENTS",
    1 << 40: "MODERATE_MEMBERS"
}



def misc_all_perms(user_perms: int):
    """
    Not all permissions were included bc I didn't want all permissions to be included.

    :param user_perms: User permissions as an integer.
    :return: A list containing every present permission's name or ADMIN.
    """
    _targets = [1, 2, 3, 4, 5, 7, 17, 22, 23, 24, 27, 28, 30, 33, 40]
    if bool(user_perms & (1 << 3)):
        return ["`ADMIN`"]
    return [f"`{PERMS_DICT.get(1 << i)}`" for i in _targets if not bool(user_perms & (1 << i))]

print(misc_all_perms(4398046511103))