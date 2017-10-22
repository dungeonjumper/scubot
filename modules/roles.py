import discord
import shlex
from modules.botModule import BotModule


class Roles(BotModule):
    name = 'Roles'

    description = 'Allow for the assignment and removal of roles.'

    help_text = 'Usage: `!roles "role_name"`. This will add you to that role if allowed.'
                ' Executing it when you already have the role assigned will remove you'
                ' from that role.')

    trigger_string = '!role'  # String to listen for as trigger

    async def parse_command(self, message, client):
        server_roles = message.server.roles  # Grab a list of all roles as Role objects
        server_roles_str = [x.name for x in server_roles]  # String-ify it into their names
        msg = shlex.split(message.content)
        role = [i for i, x in enumerate(server_roles_str) if x == msg[1]]  # Check where in the list the role is
        role_to_assign = message.server.roles[role[0]]
        if len(msg) != 1:
            try:
                if role_to_assign in message.author.roles:
                    await client.remove_roles(message.author, role_to_assign)
                    msg = ":ok_hand: Removed you from " + role_to_assign.name + " ."
                else:
                    await client.add_roles(message.author, role_to_assign)
                    msg = ":ok_hand: Added you to " + role_to_assign.name + " ."
            except discord.DiscordException:
                msg = "I'm sorry " + message.author.name + " ,I'm afraid I can't do that."
            await client.send_message(message.channel, msg)
        else:
            pass
