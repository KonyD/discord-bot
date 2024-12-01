from discord.ext import commands
import random

class EightBallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball', help='Asks the magic 8-ball a question.')
    async def magic_eightball(self, ctx):
        try:
            with open("8ball.txt", "r", encoding="utf-8") as file:
                responses = file.readlines()
                response = random.choice(responses)
                await ctx.send(response.strip())
        except Exception as e:
            print(f"Error: {e}")

async def setup(bot):
    await bot.add_cog(EightBallCog(bot))
