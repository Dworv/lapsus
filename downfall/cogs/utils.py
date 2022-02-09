
import random
import interactions 

import config
from tools.embed import create_info_embed, create_error_embed


class Utils(interactions.Extension):

    def __init__(self, client: interactions.Client):
        self.client: interactions.Client = client
    
    @interactions.extension_command(
        name="ping", 
        description="Pings the bot", 
        scope=[config.Guild.ID]
    )
    async def ping(self, ctx: interactions.CommandContext):
        await ctx.send(embeds=create_info_embed(description="Pong!"))

    @interactions.extension_command(
        name="coin-flip", 
        description="Flips a coin", 
        scope=[config.Guild.ID])
    async def coin_flip(self, ctx: interactions.CommandContext):
        await ctx.send(embeds=create_info_embed(description=f"You flipped a coin and got **{random.choice(['heads', 'tails'])}**!"))
    
    dice_sides = ['4', '6', '8', '10', '12', '20']
    @interactions.extension_command(
        name="roll-dice", 
        description="Rolls a dice", 
        scope=[config.Guild.ID],
        options = [
            interactions.Option(
                name = 'sides',
                description = 'The number of sides on the dice',
                type = interactions.OptionType.STRING,
                choices = [interactions.Choice(name=x, value=x) for x in dice_sides],
                required = True
            )
        ]
    )
    async def roll_dice(self, ctx: interactions.CommandContext, sides: str):
        await ctx.send(embeds=create_info_embed(description=f"You rolled a **{random.randint(int(sides))} from a {sides} sided dice**!"))

def setup(client: interactions.Client):
    Utils(client)