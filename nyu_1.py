import discord
import aiml

import os

kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml",commands="LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")
    kernel.setBotPredicate("name","Nyu")
def process_responce(msg):
    print (msg)
    bot_response = kernel.respond(msg)
    print (bot_response)
    return bot_response





client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Nyu"):
        pos = message.content.find('<')
        msg = message.content[pos+1:]
        y= process_responce(msg)
        if y == "":
            y = 'Sorry I don\'t undertand that one'
        if msg.strip() == "LOAD AIML B":
            y= 'Loading basic_chat.aiml...done (0.27 seconds)'
        chat = str(y).format(message)
        await client.send_message(message.channel, chat)




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('xoxox')
