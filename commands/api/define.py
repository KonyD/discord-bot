from discord.ext import commands
import requests

class DefineCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Provides the definition of a word.\n**Example Usage**: !define <word>")
    async def define(self, ctx, *, word: str):
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}"
        try:
            response = requests.get(url, timeout=5)  # Set a timeout for the request
            if response.status_code == 200:
                data = response.json()
                # Extract the word, meaning, and example
                definition = data[0]["meanings"][0]["definitions"][0]["definition"]
                example = data[0]["meanings"][0]["definitions"][0].get("example", "No example provided.")
                part_of_speech = data[0]["meanings"][0]["partOfSpeech"]

                # Format and send the response
                await ctx.send(
                    f"📖 **Word:** {word.capitalize()}\n"
                    f"**Part of Speech:** {part_of_speech}\n"
                    f"**Definition:** {definition}\n"
                    f"**Example:** {example}"
                )
            elif response.status_code == 404:
                await ctx.send(f"❌ No definition found for the word: {word}")
            else:
                await ctx.send("❌ Failed to fetch the definition. Please try again later.")
        except requests.RequestException as e:
            await ctx.send(f"⚠️ An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(DefineCog(bot))
