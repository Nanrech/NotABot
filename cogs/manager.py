import interactions

from utils.funcs import current_time
from utils.constants import BRANDING_COLOUR


class Manager(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client

    @interactions.extension_command(name="lock",
                                    description="Locks sections of the server",
                                    options=[
                                        interactions.Option(
                                            name="channel",
                                            description="Locks a single channel. Defaults to current channel",
                                            type=interactions.OptionType.SUB_COMMAND,
                                            required=True
                                        ),
                                        interactions.Option(
                                            name="category",
                                            description="Locks an entire category. Defaults to current category",
                                            type=interactions.OptionType.SUB_COMMAND,
                                            required=True
                                        )
                                    ])
    async def i_manager_lock_channel(self, ctx: interactions.CommandContext):
        if not bool(interactions.Permissions.MANAGE_CHANNELS & ctx.author.permissions) or not bool(
                interactions.Permissions.ADMINISTRATOR & ctx.author.permissions):
            return await ctx.send(ephemeral=True,
                                  embeds=interactions.Embed(
                                      title="Insufficient permissions",
                                      description="To run this command you must have the `MANAGE_CHANNELS` or the `ADMINISTRATOR` permission!",
                                      image=interactions.EmbedImageStruct(
                                          url="https://http.cat/403"
                                      ),
                                      color=BRANDING_COLOUR
                                  ))
        await ctx.get_channel()
        if ctx.channel.type is interactions.ChannelType.GUILD_PUBLIC_THREAD or ctx.channel.type is interactions.ChannelType.GUILD_PRIVATE_THREAD:
            return await ctx.channel.modify(locked=True, reason=f"{current_time()} Locked by {ctx.author.user.username}#{ctx.author.user.discriminator}. ({ctx.author.id})")
        if ctx.channel.type not in [0, 5, 10]:
            return await ctx.send("Can't lock this type of channel",
                                  ephemeral=True)
        await ctx.channel.modify()


def setup(client):
    Manager(client)
