import interactions
import re
import aiohttp

from utils.cache import cache
from utils.constants import BRANDING_COLOUR
from utils.funcs import misc_get_chan_type, misc_all_perms

session = aiohttp.ClientSession()


class Misc(interactions.Extension):
    def __init__(self, client):
        self.client = client
        self.session = session

    @interactions.extension_command(name="avatar",
                                    description="Returns an embed containing a user's avatar",
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.USER,
                                            name="user",
                                            description="User whose avatar you want to grab. Leave blank to get your own",
                                            required=False
                                        )
                                    ])
    async def i_misc_get_avatar(self, ctx: interactions.CommandContext, user: interactions.Member = None):
        url = ctx.author.user.avatar_url if user is None else user.user.avatar_url or "https://http.cat/204"
        await ctx.send(f"{url} ** **")

    @interactions.extension_command(name="emoji",
                                    description="Shows all the emoji in this server",)
    async def i_misc_emoji_list(self, ctx: interactions.CommandContext):
        emoji_list = cache.get_cached_emojis(ctx.guild_id)
        if not emoji_list:
            cache.cache_emojis(guild_id=ctx.guild_id, contents=(await ctx.get_guild()).emojis)
            emoji_list = cache.emojis.get(ctx.guild_id)
        await ctx.send(embeds=interactions.Embed(
            title=f"Showing a total of {len(emoji_list)} emojis",
            description=f"""{' '.join([f'<{"a" if emoji.get("animated") else ""}:{emoji.get("name")}:{emoji.get("id")}>' for emoji in emoji_list])}""",
            color=BRANDING_COLOUR
        ))

    @interactions.extension_command(name="invite-info",
                                    description="Returns some info about an invite",
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.STRING,
                                            required=True,
                                            name="invite",
                                            description="The invite you want to analyze"
                                        )
                                    ])
    async def i_misc_invite_info(self, ctx: interactions.CommandContext, invite: str):
        code = invite
        if "https://discord.gg/" in invite or "discord.gg/" in invite:
            code = invite.split(".gg/")[1]

        if "https://discord.com/invite/" in invite:
            code = invite.split("invite/")[1]

        if bool(re.search("[^a-zA-Z0-9-]", code)):
            return await ctx.send(embeds=interactions.Embed(
                title="Invalid code",
                description=f"Command accepts '`https://discord.gg/*`', '`discord.gg/*`' or just an invite code ('`discord-developers`')\n\nCode: '`{code}`'. See cat pic below for more info.",
                color=BRANDING_COLOUR,
                image=interactions.EmbedImageStruct(
                    url="https://http.cat/400"
                )
            ))

        async with session.get(f"https://discord.com/api/v10/invites/{code}") as resp:
            if resp.status != 200:
                return await ctx.send(embeds=interactions.Embed(
                    title="Invalid code",
                    description=f"Code: '`{code}`'. See cat pic below for more info.",
                    color=BRANDING_COLOUR,
                    image=interactions.EmbedImageStruct(
                        url=f"https://http.cat/{resp.status}"
                    )
                ))
            raw: dict = await resp.json()
            typechan = misc_get_chan_type(raw['channel']['type'])
            embed = interactions.Embed(
                title=f"`{code}`: {raw['guild']['name']} ({raw['guild']['id']})",
                url=f"https://discord.gg/{raw['code']}",
                color=BRANDING_COLOUR,
                description=f"Invite expiration: {raw['expires_at'] or 'null'}",
                fields=[
                    interactions.EmbedField(
                        name=f"**`{typechan}`** ({raw['channel']['id']})",
                        value=f"#{raw['channel']['name']} <#{raw['channel']['id']}>"
                    ),
                    interactions.EmbedField(
                        name="**Server Description**",
                        value=raw['guild']['description'] or "[No description](https://http.cat/204)"
                    )
                ]
            )
            embed.set_thumbnail(
                url=f"https://cdn.discordapp.com/icons/{raw['guild']['id']}/{raw['guild']['icon']}{'.gif' if '_a' in raw['guild']['icon'] else '.png'}" if
                raw['guild']['icon'] else "https://http.cat/204")
        return await ctx.send(embeds=embed)

    @interactions.extension_command(name="whois",
                                    description="Shows some info on a member.",
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.USER,
                                            name="user",
                                            description="N/A",
                                            required=False
                                        )
                                    ])
    async def i_misc_whois(self, ctx: interactions.CommandContext, user: interactions.Member = None):
        user = user or ctx.author
        user_embed = interactions.Embed(
            title=f"{user.user.username}#{user.user.discriminator} ({user.id})",
            description=f"Created: <t:{user.id.epoch}:R> \nJoined <t:{int(user.joined_at.timestamp())}:R>",
            thumbnail=interactions.EmbedImageStruct(
                url=user.user.avatar_url or "https://http.cat/204"
            ),
            color=BRANDING_COLOUR,
            fields=[
                interactions.EmbedField(
                    name="Nickname",
                    value=f"{'`No`' if not user.nick else user.nick}",
                    inline=True
                ),
                interactions.EmbedField(
                    name=f"Roles: {len(user.roles)}",
                    value=f"{', '.join([f'<@&{role}>' for role in user.roles]) if len(user.roles) != 0 else '** **'}",
                    inline=True
                ),
                interactions.EmbedField(
                    name="Permissions",
                    value=", ".join(misc_all_perms(int(user.permissions))) + "** **"
                )
            ]
        )
        return await ctx.send(embeds=user_embed)


def setup(client):
    Misc(client)
