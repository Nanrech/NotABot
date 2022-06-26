import json

from pathlib import Path
from os import getenv
from dotenv import load_dotenv

with open(Path("cfgs/config.json").absolute(), "r") as f:
    _json = json.load(f)

load_dotenv()
# BOT_TOKEN = _json.get("token")
BOT_TOKEN = getenv("__BOT_TOKEN_VERY_PRIVATE")
PREFIX = _json.get("prefix")
ADMIN = _json.get("ownerID")
SCOPE = _json.get("guildID")
N_GUILDS = "global" if len(SCOPE) == 0 else len(SCOPE)
_CHANS = _json.get("important_channels")
ANNOUNCEMENTS = _CHANS.get("announcements")
BOT_CHANS = _CHANS.get("bots_allowed")
BRANDING_COLOUR = 0xf74949
CHAN_TYPES = {
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
