import discord
import os
#import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

# default permissions + message_content (lets us send messages)
intents = discord.Intents.default()
intents.message_content= True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# bot wrapper for commands
bot = commands.Bot(command_prefix='$', intents=intents)

# put this before every bot command a user can put into the chat 
# ctx (context) is always the first argument, arg (or something like: arg1, arg2 or args*) is user input
@bot.command()
async def hello(ctx, arg):
    print("Sending Message...")
    await ctx.send("Hello " + arg)
    print("Message Sent")

bot.run(TOKEN)
client.run(TOKEN)
