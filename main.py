import discord
import os
#import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

#permissions object
intents = discord.Intents.default()
intents.message_content= True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

pending_invites = {}
active_games = {}

#bot wrapper for commands
bot = commands.Bot(command_prefix='/', intents=intents)

#put this before every bot command a user can put into the chat 
#ctx (context) is always the first argument, arg (or something like: arg1, arg2 or args*) is user input
@bot.command()
async def play(ctx, member: discord.User):
    #make sure the user is on the server, if not it throws an error
    user = bot.get_guild(ctx.message.guild.id).get_member(member.id)
    
    pending_invites[ctx.message.author.name] = user.name
    
    await ctx.send("Hi! " + user.mention + " you're being challenged to a chess game. Type '/accept [username]' to play or '/deny [username]' to reject the invite")

#This is how to do error handling for the discord bot: 
@play.error
async def play_error(ctx, error):
    await ctx.send("Can't seem to find them. Guess you can't play chess :(")

@bot.command()
async def accept(ctx, member: discord.User):
    user = bot.get_guild(ctx.message.guild.id).get_member(member.id)
    
    active_games[user.name] = ctx.message.author.name
    pending_invites.pop(user.name)
    
    await ctx.send("Game Invitation Accepted")

@accept.error
async def accept_error(ctx, error):
    print(error)
    await ctx.send("Guess I lost that game invite :/")

@bot.command()
async def deny(ctx, member: discord.User):
    user = bot.get_guild(ctx.message.guild.id).get_member(member.id)
    
    pending_invites.pop(user.name)
    
    await ctx.send("Game Invitation Denied")

@deny.error
async def deny_error(ctx, error):
    print(error)
    await ctx.send("Guess I lost that game invite :/")

@bot.command()
async def debugInvites(ctx):
    print(pending_invites)

bot.run(TOKEN)
client.run(TOKEN)
