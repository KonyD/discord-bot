import discord
from discord.ext import commands
import time

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()  # Record when the bot starts

    @commands.command(name="status", help="Displays the bot's status, latency, and uptime.")
    async def status(self, ctx):
        # Calculate uptime
        current_time = time.time()
        uptime_seconds = int(current_time - self.start_time)
        uptime = self.format_uptime(uptime_seconds)

        # Get bot latency
        latency = round(self.bot.latency * 1000)  # Latency in ms

        # Create an embed for a nicer display
        embed = discord.Embed(title="Bot Status", color=discord.Color.green())
        embed.add_field(name="Latency", value=f"{latency} ms", inline=True)
        embed.add_field(name="Uptime", value=uptime, inline=True)
        embed.set_footer(text="Bot Status Command")
        
        await ctx.send(embed=embed)

    def format_uptime(self, seconds):
        """Converts uptime in seconds to a human-readable format."""
        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        parts = []
        if days > 0:
            parts.append(f"{days}d")
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        parts.append(f"{seconds}s")
        return " ".join(parts)

async def setup(bot):
    await bot.add_cog(StatusCog(bot))
