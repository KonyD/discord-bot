from discord.ext import commands
import requests

class MemeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='meme', help='Sends a random meme.')
    async def send_random_meme(self, ctx):
        try:
            # Fetch a random meme using the meme API
            response = requests.get("https://meme-api.com/gimme")

            if response.status_code == 200:
                data = response.json()
            
                if "url" in data:
                    meme_url = data["url"]
                    await ctx.send(meme_url)
                else:
                    await ctx.send("Couldn't fetch a meme. Please try again later!")
            else:
                await ctx.send(f"Failed to fetch meme. API returned status code {response.status_code}.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(MemeCog(bot))
