from discord.ext import commands
import time
import datetime

class UptimeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.startTime = time.time()

    @commands.command(help='Displays how long the bot has been running.')
    async def uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-self.startTime))))
        await ctx.send(uptime)

async def setup(bot):
    await bot.add_cog(UptimeCog(bot))
