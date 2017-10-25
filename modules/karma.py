import discord
from modules.botModule import BotModule

class Karma(BotModule):
        name = 'karma'

        description = 'Monitors messages for reactions and adds karma accordingly.'

        help_text = 'This module has no callable functions'

        trigger_string = '!reddit'

        listen_for_reaction = True

        async def parse_command(self, message, client):
            pass

        async def on_reaction(self, reaction, client):
            print("karma_action triggered")
            msg = "I saw that!" + reaction.message.author.name + reaction.emoji
            await client.send_message(reaction.message.channel, msg)