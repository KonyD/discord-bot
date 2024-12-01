from discord.ext import commands
import requests

class CatFactCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Sends a random cat fact.")
    async def catfact(self, ctx):
        url = "https://catfact.ninja/fact"
        try:
            response = requests.get(url, timeout=5)  # Set a timeout for the request
            if response.status_code == 200:
                data = response.json()
                fact = data.get("fact", "Could not fetch a cat fact at this time.")
                await ctx.send(f"🐱 Cat Fact: {fact}")
            else:
                await ctx.send("❌ Failed to fetch a cat fact. Please try again later.")
        except requests.RequestException as e:
            await ctx.send(f"⚠️ An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(CatFactCog(bot))
