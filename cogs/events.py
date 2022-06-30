# HEAVILY WIP

import interactions

from utils.cache import cache


class Events(interactions.Extension):
    def __init__(self, client):
        self.client = client

    @interactions.extension_listener(name="on_guild_emojis_update")
    async def events_emoji_cache_event(self, payload: interactions.GuildEmojis):
        cache.cache_emojis(payload.guild_id, payload.emojis)

    # TODO Add more events whenever they're necessary


def setup(client):
    Events(client)
