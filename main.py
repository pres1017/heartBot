import heart as h
import discord as d
from discord.ext import commands
from flask import Flask
from threading import Thread

app = Flask('')

#import discord
#from discord.ext.commands import has_permission
#@bot.command(pass_context=True)
#@has_permission(administrator=True)
#async def admins_only_command(ctx, *, args):
# Do stuff...

# Take back command
# Get the emojis working properly for different values
# Put pictures

# Check the value of the gift
# Check if anonymous
# Check the level of hearts
# Check if there's a comment
# Check what the gift is

#Command: /give gifter receiver gift amount anonymous comment
#/give giverID receiverID apple 5 false -I hate you
#/back giverID receiverID apple 5 5
#string = <@123654789546213>

#string = [2:(len(string) - 1)]

client = d.Client()
filename = "hearts.csv"
mainChannelId = 788897033510453259

@client.event
async def on_message(message):
  if message.content.startswith("/hhelp"):
    help_out = h.help()
    await message.channel.send(help_out)

  if message.content.startswith("/give "):

    author_is_in = False
    # role ids for roles that can access the bot, if you have more than two that should be able to access just add the 
    list_role_id = 790643321058885702
    list_role_id2 = 790642940615589919
    # list of the roles of the author who accessed the command
    list_roles = message.author.roles
    # this just iterates through the list of roles and checks the id against the approved ones, just add more or statements if needed
    for x in range(0, len(list_roles)):
      if (list_roles[x].id == list_role_id or list_roles[x].id == list_role_id2):
        author_is_in = True

    if (author_is_in):
      message1 = message.content
      num = message1.find("-")
      
      message_var = ""

      comment = ""
      comment_in = False
      if (num == -1):
        comment_in = False
      else:
        comment_in = True
      
      if comment_in == True:
        first_split = message1.split("-")
        parts = first_split[0].split(" ")

        comment = first_split[1]
      else: 
        parts = message1.split(" ")
      
      giverID = parts[1]
      #giverID = giverID.replace("<","")
      
      receiverID = parts[2]
      #receiverID = receiverID.replace("<","")
      
      gift = parts[3]
      amount = parts[4]
      gift_value = h.checkGiftValue(parts[3])
      value = str(gift_value * float(parts[4]))
      
      if (parts[5] == "t" or parts[5] == "T" or parts[5] == "True"  or parts[5] == "true"):
        anonymous = True
      else:
        anonymous = False
      
      gift_value_before = h.checkValue(giverID, receiverID, filename)

      h.changeHeart(giverID, receiverID, value, filename)

      # determines the icon/pictures for the gift
      gift_icon = h.det_icon(gift)
      gift_pic = h.det_pic(gift)
      gift_value_after = h.checkValue(giverID, receiverID, filename)
      

      gifterNick = await client.fetch_user(giverID)
      receiverNick = await client.fetch_user(receiverID)
      gifterNickID = gifterNick.name
      receiverNickID = receiverNick.name

      # determines the level of the relationship
      if anonymous == True:
        gifterNickID = "匿名老板"
      level_announcement = h.get_level(gift_value_before, gift_value_after, gifterNickID, receiverNickID)

      #anounces--------------------------

      atEveryone = ""
      if h.checkGift(value) == 1:
        AnnounceIcon = "<:682564041528442881:691351337723756545>"
      elif h.checkGift(value) == 2:
        AnnounceIcon = "<a:vbluestar:745646061854654475>"
      elif h.checkGift(value) == 3:
        atEveryone = "@everyone"
        AnnounceIcon = "<a:708890470255951883:710561625278513182>"

      if (anonymous == True):
        message_var = AnnounceIcon*3 + atEveryone + "感谢 匿名老板 给 <@" + receiverID + "> " + "赠送了" + gift_icon + gift + "*" + amount + "，:sparkling_heart:心动值达到" + str(h.checkValue(giverID, receiverID, filename))
      else: 
        message_var = AnnounceIcon*3 + atEveryone + "感谢 <@" + giverID + "> 给 <@" + receiverID + "> " + "赠送了" + gift_icon + gift + "*" + amount + "，:sparkling_heart:心动值达到" + str(h.checkValue(giverID, receiverID, filename))

      #appends the comment to the end if it exists
      if comment_in == True:
        message_var = message_var + "，并留言【" + comment + "】"

      message_var = message_var + level_announcement

      message_var = message_var + "，谢谢老板！！！" + AnnounceIcon*3

      general_channel = client.get_channel(mainChannelId)
      await general_channel.send(message_var)
      await general_channel.send(file=d.File('Gifts/' + gift_pic))
      # address = "Gifts/" + gift_pic + ".png"
      #await message.channel.send(file=d.File('Gifts/' + gift_pic + '.png'))
    else:
      message_var = "You do not have access to this bot"
      general_channel = client.get_channel(mainChannelId)
      await general_channel.send(message_var)
  
  #/back giverID receiverID apple 5 5
  if message.content.startswith("/back "):

    author_is_in = False
    list_role_id = 790643321058885702
    list_role_id2 = 790642940615589919  
    list_roles = message.author.roles
    for x in range(0, len(list_roles)):
      if (list_roles[x].id == list_role_id or list_roles[x].id == list_role_id2):
        author_is_in = True

    if (author_is_in):
      message1 = message.content
      parts = message1.split(" ")
      
      giverID = parts[1]
      
      receiverID = parts[2]
      
      gift = parts[3]
      gift_value = h.checkGiftValue(parts[3])
      value = -(gift_value * float(parts[4]))
    
      h.changeHeart(giverID, receiverID, value, filename)

# giverID, recieverID, messageID

client.run("Bot Key Goes Here")

#allowedRole = message.guild.roles.find("name", "rolename")
#if (message.member.roles.has(allowedRole.id)

#myRole = message.guild.roles.cache.get("264410914592129025")
#if (message.member.roles.cache.has(role.id))
