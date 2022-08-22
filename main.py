import interactions
# import logging

from utils.funcs import current_time
from utils.constants import BOT_TOKEN
from utils.cache import cache

# logging.basicConfig(level=logging.DEBUG)
presence = interactions.ClientPresence(
    activities=[
        interactions.PresenceActivity(
            name="over the multiverse",
            type=interactions.PresenceActivityType.WATCHING
        )
    ])
client = interactions.Client(token=BOT_TOKEN,
                             disable_sync=False,
                             presence=presence)

counter = 0


@client.event()
async def on_ready():
    global counter
    if counter == 0:
        cache.wipe_cache()
        cache.cache_first_ready()
        counter += 1
    else:
        cache.cache_last_ready()
    cache.wipe_cached_emojis()
    print(f"{current_time()} Logged in as {client.me.name}, latency: {int(client.latency)}.")


@client.command(name="ping", description="Checks if the bot is alive", )
async def i_main_ping(ctx: interactions.CommandContext):
    await ctx.send(
        f"Latency: `{int(client.latency)}ms`. Deployed: <t:{cache.internal_first_ready}:R>, last registered reconnect: {f'<t:{cache.internal_last_ready}:R>' if cache.internal_last_ready else '`null`'}.",
        ephemeral=True)


client.load("cogs.events")
client.load("cogs.fun")
client.load("cogs.info")
client.load("cogs.misc")
client.start()
