import interactions

from utils.constants import BRANDING_COLOUR


class Info(interactions.Extension):
    def __init__(self, client):
        self.client = client
        self.info_embed = interactions.Embed(
            title="NotABot's info",
            color=BRANDING_COLOUR,
            fields=[
                interactions.EmbedField(
                    name="General",
                    value="This is Nan#5809's small utility bot. You can find the source code [here](https://github.com/Nanrech/NotABot/)"
                ),
                interactions.EmbedField(
                    name="Commands",
                    value="`avatar` </avatar:991756664900423715> `emoji` </emoji:991756664900423714> \n`flip-coin` </flip-coin:991756664900423711> `info` </info:992188021736755280> \n`invite-info` </invite-info:991756664900423716> `ping` </ping:991756664900423710> \n`rock-paper-scissors` </rock-paper-scissors:991756664900423712> `whois` </whois:992486435158495273>"
                ),
                interactions.EmbedField(
                    name="More info",
                    value="Run /help {command} to get more info about a specific command!"
                )
            ]
        )

    @interactions.extension_command(name="info",
                                    description="Returns some info about this bot",
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.STRING,
                                            name="command",
                                            description="The command you want to get info of",
                                            required=False,
                                            autocomplete=True
                                        )
                                    ])
    async def i_info_bot_info(self, ctx: interactions.CommandContext, command="NA"):
        if command == "NA":
            return await ctx.send(embeds=self.info_embed)
        else:
            match command:
                case "avatar":
                    return await ctx.send(embeds=interactions.Embed(
                        title="Avatar command's help",
                        description="</avatar:991756664900423715> Returns an embed containing a user's avatar",
                        fields=[
                            interactions.EmbedField(
                                name="Arguments",
                                value="`user`: A user or a user ID"
                            )
                        ]
                    ))
                case "emoji":
                    return await ctx.send(embeds=interactions.Embed(
                        title="Emoji command's help",
                        description="</emoji:991756664900423714> Shows all the emojis in the current server",
                        fields=[
                            interactions.EmbedField(
                                name="Arguments",
                                value="`N/A`"
                            )
                        ]
                    ))
                case "flip-coin":
                    return await ctx.send(embeds=interactions.Embed(
                        title="Coin flip command's help",
                        description="</flip-coin:991756664900423711> Flips a coin",
                        fields=[
                            interactions.EmbedField(
                                name="Arguments",
                                value="`heads`: Optional value for heads. Defaults to \"heads\"\n`tails`: Optional value for tails. Defaults to \"tails\""
                            )
                        ]
                    ))
                case "info":
                    return await ctx.send(embeds=interactions.Embed(
                        title="Info command's help",
                        description="</info:992188021736755280> RecursionError: maximum recursion depth exceeded in comparison",
                        fields=[
                            interactions.EmbedField(
                                name="Arguments",
                                value="`command`: The command you want more info on"
                            )
                        ]
                    ))
                case "invite-info":
                    return await ctx.send(embeds=interactions.Embed(
                        title="Invite info command's help",
                        description="</invite-info:991756664900423716> Returns some info about an invite",
                        fields=[
                            interactions.EmbedField(
                                name="Arguments",
                                value="`invite`: The invite you want to analyze"
                            )
                        ]
                    ))
                case "ping":
                    return await ctx.send(embeds=interactions.Embed(
                        title="Ping command's help",
                        description="</ping:991756664900423710> Checks if the bot is still alive",
                        fields=[
                            interactions.EmbedField(
                                name="Arguments",
                                value="`N/A`"
                            )
                        ]
                    ))
                case "rock-paper-scissors":
                    return await ctx.send(embeds=interactions.Embed(
                        title="Rock Paper Scissors command's help",
                        description="</rock-paper-scissors:991756664900423712> Play a round of rps against the bot",
                        fields=[
                            interactions.EmbedField(
                                name="Arguments",
                                value="`choice`: Your choice. Available options = [rock, paper, scissors]"
                            )
                        ]
                    ))
                case "whois":
                    return await ctx.send(embeds=interactions.Embed(
                        title="Who-is command's help",
                        description="</whois:992486435158495273> Shows some info on a member",
                        fields=[
                            interactions.EmbedField(
                                name="Arguments",
                                value="`user`: User you want to get info from. Defaults to author"
                            )
                        ]
                    ))

    @interactions.extension_autocomplete("info", "command")
    async def info_autocomplete(self, ctx: interactions.CommandContext, value=""):
        commands = ["avatar", "emoji", "flip-coin", "info", "invite-info", "ping", "rock-paper-scissors", "whois"]
        choices = [
            interactions.Choice(name=item, value=item) for item in commands if value in item
        ]
        await ctx.populate(choices)


def setup(client):
    Info(client)
