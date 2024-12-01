import discord
from discord.ext import commands

class PollCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help="Creates a poll with reactions for voting.\n**Example usage**: `$poll What's your favorite fruit? | 🍎 🍌 🍇 🍓`")
    async def poll(self, ctx, *, input_text: str):
        try:
            # Split the input into question and emojis
            parts = input_text.split('|')
            if len(parts) < 2:
                await ctx.send("Invalid format! Use `!poll <question> | <emoji1> <emoji2> ...`")
                return

            question = parts[0].strip()
            emojis = parts[1].strip().split()

            if len(emojis) < 2:
                await ctx.send("You must provide at least two emojis for options!")
                return

            # Create an embed for the poll
            embed = discord.Embed(title="Poll", description=question, color=discord.Color.blue())
            embed.set_footer(text=f"Poll created by {ctx.author.display_name}")

            # Send the poll message and add reactions
            message = await ctx.send(embed=embed)
            for emoji in emojis:
                await message.add_reaction(emoji)

            await ctx.send(f"Poll created! React to vote using: {' '.join(emojis)}")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(PollCog(bot))