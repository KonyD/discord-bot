from discord.ext import commands

class UnbanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Unbans a user or bot by their ID.\n**Example usage**: `$unban <user ID>`")
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, userID: int):
        try:
            # Fetch the list of all bans (async generator)
            banned_users = []
            async for ban_entry in ctx.guild.bans():
                banned_users.append(ban_entry)

            # Find the banned user or bot by their ID
            user_to_unban = None
            for ban_entry in banned_users:
                if ban_entry.user.id == userID:
                    user_to_unban = ban_entry.user
                    break

            # If the user or bot isn't found in the ban list
            if user_to_unban is None:
                await ctx.send(f"No user with ID `{id}` is banned in this server.")
                return

            # Unban the user or bot
            await ctx.guild.unban(user_to_unban)
            await ctx.send(f"Unbanned **{user_to_unban.name}** (ID: {user_to_unban.id}).")

        except Exception as e:
            # Catch errors and provide feedback
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(UnbanCog(bot))
