import interactions

from random import choices, choice as random_choice
from utils.funcs import rps_get_winner, rps_get_weights


class Fun(interactions.Extension):
    def __init__(self, client):
        self.client = client
        self.rps: dict = {
            "r": "rock :right_facing_fist:",
            "p": "paper :hand_splayed:",
            "s": "scissors :v:"
        }

    # NOTE The rock-paper-scissors minigame is "rigged". Look at funcs.rps_get_weighs for more info
    @interactions.extension_command(name="rock-paper-scissors",
                                    description="Play a round of rock paper scissors against the bot",
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.STRING,
                                            name="choice",
                                            description="Your choice",
                                            required=True,
                                            choices=[
                                                interactions.Choice(
                                                    name="rock",
                                                    value='r'
                                                ),
                                                interactions.Choice(
                                                    name="paper",
                                                    value='p'
                                                ),
                                                interactions.Choice(
                                                    name="scissors",
                                                    value='s'
                                                )
                                            ]
                                        )
                                    ]
                                    )
    async def i_fun_rock_paper_scissors(self, ctx: interactions.CommandContext, choice: str):
        weights = rps_get_weights(choice)
        user_choice = self.rps.get(choice)
        choice_b = choices(list(self.rps.keys()), weights=weights)[0]
        bot_choice = self.rps.get(choice_b).replace("right", "left")
        win_state = rps_get_winner(choice, choice_b)
        return await ctx.send(f"• You chose {user_choice}\n• I chose {bot_choice} \n> **`You {win_state}`**",
                              ephemeral=False)

    @interactions.extension_command(name="flip-coin",
                                    description="Flips a coin",
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.STRING,
                                            required=False,
                                            name="heads",
                                            description="Defaults to 'heads'. Optional alternative name for the first coinflip option."
                                        ),
                                        interactions.Option(
                                            type=interactions.OptionType.STRING,
                                            required=False,
                                            name="tails",
                                            description="Defaults to 'tails'. Optional alternative name for the second coinflip option."
                                        )
                                    ])
    async def i_fun_flip(self,
                         ctx: interactions.CommandContext,
                         heads="HEADS :slight_smile:",
                         tails="TAILS :upside_down:"):
        result = random_choice([heads, tails])
        await ctx.send(f"Coin flipped. Result: **{result[:100]}**")


def setup(client):
    Fun(client)
