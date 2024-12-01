from discord.ext import commands
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

class WeatherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Fetches current weather information for the specified city.\n**Example usage**: `$weather istanbul`")
    async def weather(self, ctx, city=None):
        if not API_KEY:
            await ctx.send("API key is missing. Please set it in your .env file.")
            return
        
        if not city:
            await ctx.send("Oops! You forgot to include a city name. Usage: `$weather <city>`")
            return
        
        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            )
            if response.status_code == 200:
                data = response.json()
                city_name = data['name']
                weather_desc = data['weather'][0]['description']
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']

                await ctx.send(
                    f"Weather in {city_name}:\n"
                    f"- Description: {weather_desc}\n"
                    f"- Temperature: {temp}°C\n"
                    f"- Feels Like: {feels_like}°C"
                )
            else:
                error_message = response.json().get("message", "An error occurred.")
                await ctx.send(f"Could not fetch weather data: {error_message}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(WeatherCog(bot))
