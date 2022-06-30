import interactions

from utils.constants import BRANDING_COLOUR


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
                    name="General info",
                    value="To be filled at a later date..."
                )
            ]
        )

    @interactions.extension_command(name="info",
                                    description="Returns some info about this bot",)
    async def i_info_bot_info(self, ctx: interactions.CommandContext):
        await ctx.send("Look at DMs!", ephemeral=True)
        final_embed = self.info_embed
        final_embed.description = f"Message sent from {(await ctx.get_guild()).name} ({ctx.guild_id})"
        return await ctx.author.send(embeds=final_embed)


def setup(client):
    Info(client)
