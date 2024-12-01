from discord.ext import commands

class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Bans a user from the server.\n**Example usage**: `$ban <user ID>`")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, userID: int, reason=None):
        user = ctx.guild.get_member(userID)
        
        if user is None:
            await ctx.send(f"Could not find the user with ID {id} in this server.")
            return

        message = reason if reason else "No reason given"
        await user.kick(reason=message)
        await ctx.send(f"**{user.name}** has been banned from **{ctx.guild.name}**.")

async def setup(bot):
    await bot.add_cog(BanCog(bot))