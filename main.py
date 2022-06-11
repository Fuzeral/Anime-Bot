import discord
from discord.ext import commands
from bot_prefix import prefix
from bot_token import token
from guild_ids import guilds
import os
import sys
import traceback
import json


client = commands.Bot(command_prefix=f"{prefix}")


@client.event
async def on_ready():
    print("Bot Online[\]")



@client.slash_command(guild_ids = [983736213443846204])
async def ping(ctx):
    embed = discord.Embed(
        title = "Pong!",
        colour = discord.Colour.blue()
    )
    await ctx.respond(embed=embed)

#modules Importing
with open ('./config/modules.json', 'r') as f:
    cogsData = json.load(f)
    module = cogsData['extensions']

if __name__ == "__main__":
    for values in module:
        try:
            client.load_extension(values)
            print(f"[/] loaded | {values}")
        except:
            print(f'Error loading {values}', file=sys.stderr)
            traceback.print_exc()

client.run(token)