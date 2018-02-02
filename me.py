#some imports are useless...for now
import discord
import random
import requests
import asyncio
import time
import re
import json
import sys

#create instance of dicksword client
me = discord.Client()

#set prefix here
prefix = "k#"

#handle message events here
@me.event
async def on_message(message):

    #check to see bot can only respond to you
    if not message.author.id == "INSERT YOUR ID HERE": return
    
    #Check for commands/prefix in message to start
    if message.content.startswith(prefix):
    
        #split message into command and arguement
        msg = message.content.split(" ", 1)
        if len(msg) > 1:
            command, args = msg[0], msg[1] 
        else:
            command, args = msg[0], ""
        command = command[2:]

        #commands here
        if command == "embed":
            await me.delete_message(message)
            fancy = discord.Embed(title = args, description = '', colour=0xDEADBF)
            fancy.set_author(name = 'Kito', icon_url = me.user.avatar_url)
            fancy.set_thumbnail(url = "https://cdn.discordapp.com/emojis/403695960347246593.png")
            fancy.set_footer(text="My dick hurts", icon_url=discord.Embed.Empty)
            await me.send_message(message.channel, embed = fancy)

#Start the bot
me.run("LOCAL STORAGE TOKEN GOES HERE", bot = False)
