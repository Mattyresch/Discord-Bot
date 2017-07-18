import discord
from discord.ext.commands import Bot
from utils import *

my_bot = Bot(command_prefix="!")

@my_bot.event
async def on_read():
    print("Client logged in")

@my_bot.command()
async def hello(*args):
    return await my_bot.say("Hello, world!")

@my_bot.command()
async def usage(*argv):
    if len(argv) < 1:
        return await getUsage(my_bot, " ")
    else:
        return await getUsage(my_bot, argv[0])

@my_bot.command()
async def search(searchtype, time, sr_name, keyword):
    return await searchSR(my_bot, searchtype, time, sr_name, keyword)

@my_bot.command()
async def soccer(time):
    return await soccerSearch(my_bot, time)

@my_bot.command()
async def redditrecap(time):
    return await recap(my_bot, time)

@my_bot.command()
async def redditRecap(time):
    return await recap(my_bot, time)

@my_bot.command()
async def tweets():
    return await getTweets(my_bot)

my_bot.run("")
