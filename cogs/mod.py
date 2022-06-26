import interactions

from cfgs.constants import SCOPE


class Mod(interactions.Extension):
    def __init__(self, client):
        self.client = client

    @interactions.extension_command(name="ban",
                                    description="Bans a user",
                                    scope=SCOPE,
                                    options=[
                                        interactions.Option(
                                            type=interactions.OptionType.USER,
                                            name="target",
                                            description="User that'll get beamed",
                                            required=True
                                        )
                                    ])
    async def i_mod_ban(self, ctx: interactions.CommandContext, target):
        ...

def setup(client):
    Mod(client)
