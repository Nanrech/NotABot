# HEAVILY WIP
import interactions

from utils.constants import BRANDING_COLOUR
from utils.funcs import current_time


class Mod(interactions.Extension):
    def __init__(self, client):
        self.client = client

    @interactions.extension_command(name="ban",
                                    description="Bans a user",
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.USER,
                                            name="target",
                                            description="User that'll get banned",
                                            required=True
                                        ),
                                        interactions.Option(
                                            type=interactions.OptionType.STRING,
                                            name="reason",
                                            description="Reason for the ban. This is the reason that'll show up in the Audit Log. Defaults to null",
                                            required=False
                                        ),
                                        interactions.Option(
                                            type=interactions.OptionType.INTEGER,
                                            name="delete_message_days",
                                            description="How many days worth of target's messages are to be deleted. Defaults to 0"
                                        )
                                    ])
    async def i_mod_ban(self, ctx: interactions.CommandContext, target: interactions.Member, reason: str = None,
                        delete_message_days: int = 0):
        if int(ctx.guild_id) != 749015533310967828:
            return await ctx.send("Nope! This experiment hasn't been rolled out to your server yet. Wait a minute!",
                                  ephemeral=True)
        if not bool(interactions.Permissions.BAN_MEMBERS & ctx.author.permissions) or not bool(
                interactions.Permissions.ADMINISTRATOR & ctx.author.permissions
                or not bool(interactions.Permissions.MODERATE_MEMBERS & ctx.author.permissions)):
            return await ctx.send(ephemeral=True,
                                  embeds=interactions.Embed(
                                      title="Insufficient permissions",
                                      description="To run this command you must have the `BAN_MEMBERS`, `MODERATE_MEMBERS` or `ADMINISTRATOR` permission!",
                                      image=interactions.EmbedImageStruct(
                                          url="https://http.cat/403"
                                      ),
                                      color=BRANDING_COLOUR
                                  ))
        await target.ban(guild_id=int(ctx.guild_id),
                         reason=f"{current_time()} Banned by {ctx.author.user.username}#{ctx.author.user.discriminator} ({ctx.author.id}). Reason: {reason or 'null'}",
                         delete_message_days=delete_message_days)
        await ctx.send(embeds=interactions.Embed(
            title=f"Banned {target.user.username}#{target.user.discriminator}",
            description=f"Moderator: {ctx.author.user.username}#{ctx.author.user.discriminator} `{ctx.author.id}` \nUser ID: `{target.id}`",
            thumbnail=interactions.EmbedImageStruct(
                url=target.user.avatar_url or "https://http.cat/204"
            ),
            color=BRANDING_COLOUR
        ))

    @interactions.extension_command(name="kick",
                                    description="Kicks a user",
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.USER,
                                            name="target",
                                            description="User that'll get kicked",
                                            required=True
                                        ),
                                        interactions.Option(
                                            type=interactions.OptionType.STRING,
                                            name="reason",
                                            description="Reason for the kick. This is the reason that'll show up in the Audit Log. Defaults to null",
                                            required=False
                                        )
                                    ])
    async def i_mod_kick(self, ctx: interactions.CommandContext, target: interactions.Member, reason: str = None):
        if int(ctx.guild_id) != 749015533310967828:
            return await ctx.send("Nope! This experiment hasn't been rolled out to your server yet. Wait a minute!",
                                  ephemeral=True)
        if not bool(interactions.Permissions.KICK_MEMBERS & ctx.author.permissions) or not bool(
                interactions.Permissions.ADMINISTRATOR & ctx.author.permissions
                or not bool(interactions.Permissions.MODERATE_MEMBERS & ctx.author.permissions)):
            return await ctx.send(ephemeral=True,
                                  embeds=interactions.Embed(
                                      title="Insufficient permissions",
                                      description="To run this command you must have the `KICK_MEMBERS`, `MODERATE_MEMBERS` or `ADMINISTRATOR` permission!",
                                      image=interactions.EmbedImageStruct(
                                          url="https://http.cat/403"
                                      ),
                                      color=BRANDING_COLOUR
                                  ))
        await target.ban(guild_id=int(ctx.guild_id),
                         reason=f"{current_time()} Kicked by {ctx.author.user.username}#{ctx.author.user.discriminator} ({ctx.author.id}). Reason: {reason or 'null'}")
        await ctx.send(embeds=interactions.Embed(
            title=f"Kicked {target.user.username}#{target.user.discriminator}",
            description=f"Moderator: {ctx.author.user.username}#{ctx.author.user.discriminator} `{ctx.author.id}` \nTarget ID: `{target.id}`",
            thumbnail=interactions.EmbedImageStruct(
                url=target.user.avatar_url or "https://http.cat/204"
            ),
            color=BRANDING_COLOUR
        ))

    @interactions.extension_command(name="mute",
                                    description="Times a user out",
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.USER,
                                            name="target",
                                            description="User that'll get timed out",
                                            required=True
                                        ),
                                        interactions.Option(
                                            type=interactions.OptionType.INTEGER,
                                            name="duration",
                                            description="How long the user will be timed out. Defaults to 'indefinite'",
                                            required=False
                                        )
                                    ])
    async def i_mod_mute(self, ctx: interactions.CommandContext, target: interactions.Member, duration):
        if int(ctx.guild_id) != 749015533310967828:
            return await ctx.send("Nope! This experiment hasn't been rolled out to your server yet. Wait a minute!",
                                  ephemeral=True)
        if not bool(interactions.Permissions.MODERATE_MEMBERS & ctx.author.permissions) or not bool(
                interactions.Permissions.ADMINISTRATOR & ctx.author.permissions):
            return await ctx.send(ephemeral=True,
                                  embeds=interactions.Embed(
                                      title="Insufficient permissions",
                                      description="To run this command you must have the `MODERATE_MEMBERS` or the `ADMINISTRATOR` permission!",
                                      image=interactions.EmbedImageStruct(
                                          url="https://http.cat/403"
                                      ),
                                      color=BRANDING_COLOUR
                                  ))
        await ctx.author.modify(int(ctx.guild_id),
                                communication_disabled_until={})


# TODO; Figure out how to [minutes, hours, days] = communication_disabled_until
def setup(client):
    Mod(client)
