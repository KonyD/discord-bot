from discord.ext import commands
import random

class RollCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll', help='Rolls a dice with the specified number of sides.\n**Example usage**: `$roll <number of faces>`')
    async def dice_roll(self, ctx, arg):
        try:
            sides = int(arg)  # Convert the argument to an integer
            if sides < 1:  # Check for invalid number of sides
                await ctx.send("Please enter a number greater than 0.")
                return
            
            rn = random.randint(1, sides)  # Roll the dice
            await ctx.send(f'🎲 You rolled: {rn}')
        except ValueError:
            await ctx.send("Please enter a valid number.")

async def setup(bot):
    await bot.add_cog(RollCog(bot))
