import json
import interactions

from typing import Union
from datetime import datetime


class Cache:
    def __init__(self):
        self.internal = None
        self.internal_first_ready = None
        self.internal_last_ready = None
        with open("cache/emoji.json", "r") as f:
            self.emojis: dict = json.load(f)

    def cache_emojis(self, guild_id: Union[int, str], contents: list):
        guild_id = str(guild_id)
        with open("cache/emoji.json", "r") as f:
            self.emojis = json.load(f)

        if guild_id in self.emojis.keys():
            self.emojis.pop(guild_id)

        self.emojis[guild_id] = [emoji._json if isinstance(emoji, interactions.Emoji) else emoji for emoji in contents]

        with open("cache/emoji.json", "w") as f:
            json.dump(self.emojis, f)

        return self.emojis

    def get_cached_emojis(self, guild_id: Union[int, str]):
        guild_id = str(guild_id)
        if guild_id not in self.emojis.keys():
            return False
        if len(self.emojis.get(guild_id)) == 0:
            return False
        else:
            return self.emojis.get(guild_id)

    def cache_first_ready(self):
        with open("cache/internal.json", "r") as f:
            internal = json.load(f)
        self.internal = internal
        self.internal["first_ready"] = int(datetime.now().timestamp())
        with open("cache/internal.json", "w") as f:
            json.dump(self.internal, f)
        self.internal_first_ready = self.internal["first_ready"]

    def cache_last_ready(self):
        with open("cache/internal.json", "r") as f:
            internal = json.load(f)
        self.internal = internal
        self.internal["last_ready"] = int(datetime.now().timestamp())
        with open("cache/internal.json", "w") as f:
            json.dump(self.internal, f)
        self.internal_last_ready = self.internal["last_ready"]


cache = Cache()
