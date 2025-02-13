import discord
import os

TOKEN = os.getenv("TOKEN")  # Gets the bot token from Railway environment variables

# Set up bot
intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run(TOKEN)