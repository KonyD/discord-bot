from discord.ext import commands
import discord

class UserInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userinfo', help="Shows details about a user.\n**Example usage**: `$userinfo <user ID>`")
    async def user_info(self, ctx, userID: int):
        try:
            user = await self.bot.fetch_user(userID)  # Fetch detailed user info
            if user is None:
                await ctx.send('User not found ❌')
                return
            
            embed = discord.Embed(
                title=f"{user.name}#{user.discriminator}", 
                description=f"Information about {user.name}", 
                color=discord.Color.magenta(),
                timestamp=ctx.message.created_at  # Adds timestamp to the embed
            )
            
            avatar_url = user.avatar.url if user.avatar else "https://cdn.discordapp.com/embed/avatars/0.png"
            embed.set_thumbnail(url=avatar_url)
            
            embed.add_field(name='🆔 User ID', value=f"{user.id}", inline=True)
            embed.add_field(name='🏳️ Public Flags', value=f"{user.public_flags}", inline=True)
            
            embed.add_field(name='📅 Account Created', value=user.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=True)
            
            if ctx.guild:
                member = ctx.guild.get_member(user.id)
                if member:
                    embed.add_field(name='📅 Joined Server', value=member.joined_at.strftime('%Y-%m-%d %H:%M:%S'), inline=True)
                    roles = [role.mention for role in member.roles[1:]]  # Exclude @everyone role
                    embed.add_field(name='🏷️ Roles', value=', '.join(roles) if roles else 'None', inline=False)
                    embed.add_field(name='🌟 Boosting?', value='Yes' if member.premium_since else 'No', inline=True)
                    embed.add_field(name='🛡️ Status', value=str(member.status).title(), inline=True)
            
            footer_avatar = ctx.author.avatar.url if ctx.author.avatar else "https://cdn.discordapp.com/embed/avatars/0.png"
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=footer_avatar)

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"An error occurred: {e} ❌")

async def setup(bot):
    await bot.add_cog(UserInfoCog(bot))
