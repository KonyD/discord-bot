from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='Displays a list of available commands.')
    async def help(self, ctx):
        commands_list = self.bot.commands
        help_message = "**Available Commands:**\n"
        for command in commands_list:
            help_message += f"`{self.bot.command_prefix}{command.name}`: {command.help or 'No description provided'}\n"
        await ctx.send(help_message)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
