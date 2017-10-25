import discord

from modules.units import *
from modules.roles import *
from modules.help import *
from modules.status import *
from modules.redditposts import *
from modules.karma import *

from modules.botModule import *

client = discord.Client()

BotModule.loaded_modules = [Units(), Roles(), Help(), Status(), RedditPost(), Karma()]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for bot_module in BotModule.loaded_modules:
        if message.content.startswith(bot_module.trigger_string):
            await bot_module.parse_command(message, client)


@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.author == client.user:
        return
    for bot_module in BotModule.loaded_modules:
        if bot_module.listen_for_reaction:
            await bot_module.on_reaction(reaction, client)


@client.event
async def on_ready():
    print('Login success. Your details:')
    print('User:', client.user.name)
    print('ID', client.user.id)
    print('----------')


print('scubot v' + BotModule.bot_version)
try:
    tokenFile = open('token')
except FileNotFoundError:
    print(
        'Token not found. Please make sure you have a token file in this directory. Refer to README.md for details on getting a token.')
    quit()
print('Token found. Logging in...')
token = tokenFile.read().replace('\n', '')

for bot_module in BotModule.loaded_modules:
    if bot_module.has_background_loop:
        client.loop.create_task(bot_module.background_loop(client))


client.run(token)
