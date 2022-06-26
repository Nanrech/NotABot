import interactions

from cfgs.constants import SCOPE, BRANDING_COLOUR


class Info(interactions.Extension):
    def __init__(self, client):
        self.client = client
        self.info_embed = interactions.Embed(
            title=f"{self.client.me.name}'s info",
            color=BRANDING_COLOUR,
            image=interactions.EmbedImageStruct(
                url="https://http.cat/425"
            ),
            fields=[
                interactions.EmbedField(
                    name="info",
                    value="To be filled at a later date..."
                )
            ]
        )

    @interactions.extension_command(name="bot-info",
                                    description="Returns some info about this bot",
                                    scope=SCOPE)
    async def i_info_bot_info(self, ctx: interactions.CommandContext):
        final_embed = self.info_embed
        final_embed.description = f"Message sent from {(await ctx.get_guild()).name} ({ctx.guild_id})"
        await ctx.author.send(embeds=final_embed)
        await ctx.send("<:join:879339696650600470> Look at DMs", ephemeral=True)


def setup(client):
    Info(client)
