from discord.ext import commands
import random

class FlipCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='flip', help='Flips a coin (Heads/Tails).')
    async def coin_flip(self, ctx):
        face = random.randint(1, 2)  # Generate a random number: 1 or 2
        match face:  # Use the correct variable
            case 1:
                await ctx.send('🪙 Heads')
            case 2:
                await ctx.send('🪙 Tails')

async def setup(bot):
    await bot.add_cog(FlipCog(bot))
