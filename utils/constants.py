import json


from pathlib import Path
from os import getenv
from dotenv import load_dotenv

with open(Path("utils/config.json").absolute(), "r") as f:
    _json = json.load(f)
load_dotenv()

counter = 0  # Super important variable. Do not lose.
BOT_TOKEN = getenv("__BOT_TOKEN_VERY_PRIVATE")
BRANDING_COLOUR = 0xf74949

CHAN_TYPES: dict = {
    0: "Text Channel",
    1: "DM",
    2: "Voice Channel",
    3: "Group DM",
    4: "Channel Category",
    5: "News Channel",
    10: "News Thread",
    11: "Public Thread",
    12: "Private Thread",
    13: "Stage Channel",
    14: "Server Directory",
    15: "Forums Channel"
}
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
