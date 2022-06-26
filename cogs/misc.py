import interactions
import re
import aiohttp
import json

from cfgs.constants import SCOPE, BRANDING_COLOUR
from cfgs.funcs import misc_get_chan_type

session = aiohttp.ClientSession()


class Misc(interactions.Extension):
    def __init__(self, client):
        self.client = client
        self.session = session

    @interactions.extension_command(name="show-avatar",
                                    description="Returns an embed containing a user's avatar",
                                    scope=SCOPE,
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.USER,
                                            name="user",
                                            description="User whose avatar you want to grab. Leave blank to get your own",
                                            required=False
                                        )
                                    ])
    async def i_misc_get_avatar(self, ctx: interactions.CommandContext, user: interactions.Member = None):
        url = ctx.author.user.avatar_url if user is None else user.user.avatar_url
        await ctx.send(f"{url} ** **")

    @interactions.extension_listener(name="on_guild_emojis_update")
    async def misc_emoji_cache_updater(self, payload: interactions.GuildEmojis):
        with open("cache/emoji.json", "r") as f:
            raw = json.load(f)
            raw[str(payload.guild_id)] = payload._json.get("emojis")
        with open("cache/emoji.json", "w") as f:
            json.dump(raw, f)

    @interactions.extension_command(name="emoji",
                                    description="Shows all the emoji in this server",
                                    scope=SCOPE)
    async def i_misc_emoji_list(self, ctx: interactions.CommandContext):
        with open("cache/emoji.json", "r") as f:
            json_data = json.load(f)

            if str(ctx.guild_id) in json_data.keys():
                emoji_list = json_data.get(f"{ctx.guild_id}")

            else:
                emoji_list = await self.client._http.get_all_emoji(int(ctx.guild_id))
                json_data[str(ctx.guild_id)] = emoji_list

        with open("cache/emoji.json", "w") as f:
            json.dump(json_data, f)

        print(emoji_list)
        print(json_data)
        await ctx.send(embeds=interactions.Embed(
            title=f"Showing a total of {len(emoji_list)} emojis",
            description=f"""{' '.join([f'<{"a" if emoji.get("animated") else ""}:{emoji.get("name")}:{emoji.get("id")}>' for emoji in emoji_list])}""",
            color=BRANDING_COLOUR
        ))

    @interactions.extension_command(name="invite-info",
                                    description="Returns some info about an invite",
                                    scope=SCOPE,
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
                        value=raw['guild']['description'] or "[No description found](https://http.cat/404)"
                    )
                ]
            )
            embed.set_thumbnail(
                url=f"https://cdn.discordapp.com/icons/{raw['guild']['id']}/{raw['guild']['icon']}{'.gif' if '_a' in raw['guild']['icon'] else '.png'}" if
                raw['guild']['icon'] else "https://http.cat/204")
        await ctx.send(embeds=embed)

    @interactions.extension_command(name="show-permissions",
                                    description="N/A",
                                    scope=SCOPE,
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.USER,
                                            name="user",
                                            description="N/A",
                                            required=False
                                        )
                                    ])
    async def i_misc_whois(self, ctx: interactions.CommandContext, user: interactions.Member = None):
        ...

def setup(client):
    Misc(client)
