
import random
import interactions 

import config
from tools import embed, check


class Gambling(interactions.Extension):

    def __init__(self, client: interactions.Client):
        self.client: interactions.Client = client

    # coin flip
    @interactions.extension_command(
        name="coin-flip", 
        description="Flips a coin", 
        scope=[config.Guild.ID])
    async def coin_flip(self, ctx: interactions.CommandContext):
        if illegal := check.illegal_commmand_channel(ctx.channel_id):
            await ctx.send(embeds=illegal, ephemeral=True)
            return
        embeds = embed.create_info_embed(
            description=f"You flipped a coin and got **{random.choice(['heads', 'tails'])}**!"
        )
        components = interactions.Button(
            custom_id = "gambling-coin-again",
            style = interactions.ButtonStyle.PRIMARY,
            label = "Flip Again",
        )
        await ctx.send(embeds=embeds, components=components)
    
    @interactions.extension_component('gambling-coin-again')
    async def coin_flip_again(self, ctx: interactions.ComponentContext):
        embeds = embed.create_info_embed(f"You flipped another coin and got **{random.choice(['heads', 'tails'])}**!")
        components = interactions.Button(
            custom_id = "gambling-coin-again",
            style = interactions.ButtonStyle.PRIMARY,
            label = "Flip Again",
        )
        await ctx.send(embeds=embeds, components=components)

    # dice roll
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
        if illegal := check.illegal_commmand_channel(ctx.channel_id):
            await ctx.send(embeds=illegal, ephemeral=True)
            return
        embeds = embed.create_info_embed(f"You rolled a **{random.randint(1, int(sides))}** from a **{sides}** sided dice!")
        await ctx.send(embeds=embeds)

def setup(client: interactions.Client):
    Gambling(client)