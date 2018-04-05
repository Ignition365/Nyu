import time
import discord
import asyncio
import urllib.request
import sqlite3
import aiml
import json
import request
import requests
from urllib.request import urlopen
import dataj
import os
from random import randint

client = discord.Client()
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

con = sqlite3.connect("test.db")
c = con.cursor()
c.execute(
    '''CREATE TABLE IF NOT EXISTS reminder_db(_id INTEGER PRIMARY KEY,time_stamp INTEGER NOT NULL,des TEXT NOT NULL,tunnel INTEGER NOT NULL)''')
print('name[0]')
con.commit()
con.close()
@client.event
async def on_message(message):
            # we do not want the bot to reply to itself
            if message.author == client.user:
                return
            if message.content.startswith("$c"):
                pos = message.content.find('$c')
                msg = message.content[pos + 2:]
                y = process_responce(msg)
                if y == "":
                    y = 'Sorry I don\'t undertand that one'
                if msg.strip() == "LOAD AIML B":
                    y = 'Loading basic_chat.aiml...done (0.27 seconds)'
                chat = str(y).format(message)
                await client.send_message(message.channel, chat)

            elif message.content.startswith('$reminder_'):
                print(message.channel)
                raw = message.content[10:].split(':')
                hh = raw[0].strip()
                mm =raw[1].strip()
                des = raw[2].strip()
                if des.strip() == "":
                    des="Reminder"
                a = int(time.time())
                print(hh)
                print(mm)

                if dataj.RepresentsInt(hh) and dataj.RepresentsInt(mm):
                    print("calk")
                    requried = a + int(hh) * 3600 + int(mm) * 60 - 15
                    print(requried)
                    dif = requried - a
                    if dif > 60:
                        dataj.add_reminder(requried, des,int(message.channel.id))
                    elif dif < 60:
                        msg = 'Reminder time passed !'.format(message)

                    msg = 'I will send reminder  after ' + hh + ' hours ' + mm + ' minute'.format(message)
                else:
                    msg = 'Please write in correct format \n $HH:MM:Description of Reminder'.format(message)

                await client.send_message(message.channel, msg)

            elif message.content.startswith('$help'):
                msg = '```1) For Chatting : $c[Your Chat Message]\n\n2)Setting Reminder : $reminder_HH:MM:Description\n\nExample for setting reminder in 4  hours 5 minutes \n  $reminder_04:05:Example\n\n3) $a_hug,$a_kiss,$a_slap,$a_(any thing you want Nyu to do for someone)``` '.format(message)
                await client.send_message(message.channel, msg)
            elif message.content.startswith('$a_'):
                print("hey")
                k=randint(0, 7)
                action=message.content.split(" ")[0][3:]

                # set the apikey and limit
                apikey = "HPNVCWRXMK81"  # test value
                lmt = 8

                # load the user's anonymous ID from cookies or some other disk storage
                # anon_id = <from db/cookies>

                # ELSE - first time user, grab and store their the anonymous ID
                r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)

                if r.status_code == 200:
                    anon_id = json.loads(r.content)["anon_id"]
                    # store in db/cookies for re-use later
                else:
                    anon_id = ""

                # our test search
                search_term = "anime"+str(action)

                # get the top 8 GIFs for the search term using default locale of EN_US
                r = requests.get(
                    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" % (
                    search_term, apikey, lmt, anon_id))

                if r.status_code == 200:
                    # load the GIFs using the urls for the smaller GIF sizes
                    top_8gifs = json.loads(r.content)
                else:
                    top_8gifs = None

                # continue a similar pattern until the user makes a selection or starts a new search.
                rel = []
                for doc in top_8gifs['results']:
                    rel.append(doc['url'])
                try:
                    rl = rel[k]
                except IndexError:
                    rl = rel[0]
                if not message.mentions:
                    msg = 'Who are you trying to '+ action
                    e = discord.Embed(title=action, description=msg, colour=0xDEADBF)

                else:
                    msg = message.mentions[0].mention + ' you  got a '+action+' from '+ message.author.mention +'\n'+ rl.format(message)

                    print (rl)
                await client.send_message(message.channel, msg)


async def my_background_task():
    await client.wait_until_ready()
    counter = 0

    while not client.is_closed:
        now = time.time()
        now = int(now / 100)
        print(now)

        con = sqlite3.connect("test.db")

        c = con.cursor()
        for row in c.execute('SELECT time_stamp FROM reminder_db'):
            print(row)
            print("bg_tup")
            k = row[0] / 100
            print(k)
            print("tup")
            if int(k) == now:
                print("came here")
                c.execute('SELECT des FROM reminder_db WHERE time_stamp=?', (row))
                dss=c.fetchall()
                c.execute('SELECT _id FROM reminder_db WHERE time_stamp=?', (row))
                id = c.fetchall()
                c.execute('SELECT tunnel FROM reminder_db WHERE time_stamp=?', (row))
                channel_id= c.fetchall()

                embed = discord.Embed(title="Reminder", description=str(dss[0][0]), color=0x00ff00)
                embed.set_author(name='Nyu', icon_url='https://i.ytimg.com/vi/9L6u5i5C9bo/hqdefault.jpg')
                await client.send_message( discord.Object(id=str(channel_id[0][0])), embed=embed)
                dataj.delete_reminder(id[0][0])
        counter+=1
        print (counter)
        await asyncio.sleep(10)  # task runs every 10 seconds


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(my_background_task())
client.run('NDI2MDQ3MTIwNzgxMzQ0NzY4.DafLBA.rC5XDqBsOUTy1qVe8dwD-tTsct8')