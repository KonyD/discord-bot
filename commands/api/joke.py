from discord.ext import commands
import requests

class JokeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Fetches a random joke.")
    async def joke(self, ctx):
        url = "https://official-joke-api.appspot.com/random_joke"
        try:
            response = requests.get(url, timeout=5)  # Set a timeout for the request
            if response.status_code == 200:
                data = response.json()
                setup = data.get("setup", "Oops, no setup found.")
                punchline = data.get("punchline", "No punchline? That's the joke!")
                await ctx.send(f"😂 **Joke:** {setup}\n**Punchline:** {punchline}")
            else:
                await ctx.send("❌ Failed to fetch a joke. Please try again later.")
        except requests.RequestException as e:
            await ctx.send(f"⚠️ An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(JokeCog(bot))
