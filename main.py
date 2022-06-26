import interactions
import logging

from cfgs.funcs import current_time
from cfgs.constants import BOT_TOKEN, SCOPE, N_GUILDS

# logging.basicConfig(level=logging.DEBUG)
client = interactions.Client(token=BOT_TOKEN,
                             disable_sync=True)


@client.event()
async def on_ready():
    print(f"{current_time()} Logged in as {client.me.name}. Latency: {int(client.latency)}. Scope: {N_GUILDS}")


@client.command(name="ping", description="Checks if the bot is alive", scope=SCOPE)
async def i_main_ping(ctx: interactions.CommandContext):
    await ctx.send(f"{current_time()} - {int(client.latency)}ms")


client.load("cogs.fun")
client.load("cogs.info")
client.load("cogs.misc")
client.start()
