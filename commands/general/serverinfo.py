from discord.ext import commands
import discord

class ServerInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='serverinfo', help='Displays information about the server.')
    async def server_info(self, ctx):
        embed = discord.Embed(
            title=f"{ctx.guild.name} Info", 
            description="Information of this Server", 
            color=discord.Color.blue()
        )
        embed.add_field(name='🆔 Server ID', value=f"{ctx.guild.id}", inline=True)
        embed.add_field(name='📆 Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
        embed.add_field(name='👑 Owner', value=f"{ctx.guild.owner}", inline=True)
        embed.add_field(name='👥 Members', value=f"{ctx.guild.member_count} Members", inline=True)
        embed.add_field(name='💬 Channels', value=f"{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice", inline=True)
        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else "")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ServerInfoCog(bot))
