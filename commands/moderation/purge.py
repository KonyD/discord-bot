from discord.ext import commands

class PurgeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, help="Deletes a specified number of messages in the channel.\n**Example usage**: `$purge <message count>`")
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        await ctx.message.delete()  # Delete the command message first
        deleted = await ctx.channel.purge(limit=limit)
        await ctx.send(f"Cleared {len(deleted)} messages by **{ctx.author.name}**.", delete_after=5)  # Auto-delete confirmation after 5 seconds

async def setup(bot):
    await bot.add_cog(PurgeCog(bot))
