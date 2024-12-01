from discord.ext import commands
import asyncio

class ReminderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Sets a reminder\n**Example usage**: `$remindme 2h Take a break`")
    async def remindme(self, ctx, time, *, message: str):
        try:
            unit_multipliers = {'s': 1, 'm': 60, 'h': 3600}
            duration = int(time[:-1]) * unit_multipliers[time[-1].lower()]

            if duration < 0:
                await ctx.send("Time must be a positive integer!")
                return
            
            await ctx.send(f"Reminder set for {time} from now!")
            await asyncio.sleep(duration)
            await ctx.send(f"⏰ Reminder: {message}")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

# Setup function for the cog
async def setup(bot):
    await bot.add_cog(ReminderCog(bot))  # Ensure this is awaited
