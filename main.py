import discord
import os
from discord.ext import commands
from googletrans import Translator
import giphy_client
from giphy_client.rest import ApiException
import random
import re
import asyncio
import datetime
import time
import json
import requests
from discord.ext import commands
from discord import app_commands
from wordlist import list_of_word

intents = discord.Intents.all()
client = discord.Client(intents=intents)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=['pls ', 'Pls ', 'p', 'P', 'p ', 'P ', 'Pls'], intents = intents)

    async def setup_hook(self):
        await self.tree.sync(guild = discord.Object(id = 819630334491754547))
        print(f"Synced slash commands for {self.user}.")
    
    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)

bot = Bot()


@bot.event
async def on_message(message):
  channel = bot.get_channel(904434928303882251)
  embed=discord.Embed(colour=discord.Colour.gold())
  embed.set_author(name=f"User Info ~ {message.author}")
  embed.add_field(name="Message: ", value=message.content, inline=False)
  if message.author != bot.user and message.channel == message.author.dm_channel:
        await channel.send(embed=embed)
        
  await bot.process_commands(message)

winlist2 = [
  'Yes',
  'No', 'Maybe', 'Yes Daddy', 'Yes Mommy', 'Possibly', "We'll never know", 'You Wish', "Even I can't answer that", 'Never' ]

@bot.hybrid_command(name = "8ball", with_app_command = True, description = "8ball")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def ball(ctx, *,question):
  winlistx = random.choice(winlist2)
  await ctx.send(winlistx)
	
@bot.hybrid_command(name = "pick", with_app_command = True, description = "randomly pick items from list")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def ball(ctx, num, items):
    list = items.split()
    num = int(num)
    picking = random.sample(list, num)
    listToStr = ' '.join(map(str, picking))
    await ctx.send(listToStr)

class fetch_emoji(discord.ui.View):
    def __init__(self, emojicontent, *, timeout=30, ):
        super().__init__(timeout=timeout)
        self.name = 1
        all_int = ":0123456789><"
        final_fix_bruh = ("".join(list(filter(lambda x:x in all_int, emojicontent))).replace("<", ":").replace(">",":").split(":"))
        filter_content = [ele for ele in final_fix_bruh if ele.strip()]
        filter_content_final = [x for x in filter_content if "@" not in x]
        self.emojis_main = [item for item in filter_content_final if (len(item)) > 6]
    @discord.ui.button(label="Next Emoji",style=discord.ButtonStyle.green)
    async def gray_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        self.default_ext = ".gif"
        url = f"https://cdn.discordapp.com/emojis/{self.emojis_main[self.name]}{self.default_ext}"
        url_check = requests.head(url).status_code
        print(url_check)
        if url_check != 200:
           self.default_ext =  ".png"
        elif url_check != 200:
                self.default_ext = ".jpg"
        else:
                pass
        
        embed = discord.Embed(title = "Stolen Emojis", color = discord.Colour.red())
        url = f"https://cdn.discordapp.com/emojis/{self.emojis_main[self.name]}{self.default_ext}"
        embed.set_image(url = url)
        embed.set_footer(text=f"Emojis: {self.name + 1}/{len(self.emojis_main)}") 
        print(url)
        await interaction.response.edit_message(embed = embed)
        if  self.name == (len(self.emojis_main) - 1):
            self.name = 0
        else:
            self.name = self.name + 1

@bot.hybrid_command(name = "semoji", with_app_command = True, description = "Steal emojis with message ID")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def semoji(ctx, msg_id):
    msg = await ctx.fetch_message(msg_id)
    content_of_mssg = msg.content
    ext_check = ".gif"
    all_int = ":0123456789><@"
    final_fix_bruh = ("".join(list(filter(lambda x:x in all_int, content_of_mssg))).replace("<", ":").replace(">",":").split(":"))
    filter_content = [ele for ele in final_fix_bruh if ele.strip()]
    filter_content_final = [x for x in filter_content if "@" not in x]
    emojis_main = [item for item in filter_content_final if (len(item)) > 6]
    url = f"https://cdn.discordapp.com/emojis/{emojis_main[0]}{ext_check}"
    url_check_def = requests.head(url).status_code
    print(url_check_def)
    if url_check_def != 200:
        ext_check = ".png"
    elif url_check_def != 200:
        ext_check = ".jpg"
    else:
        print("passed conditions")
        pass
    url = f"https://cdn.discordapp.com/emojis/{emojis_main[0]}{ext_check}"
    embed = discord.Embed(title = "Stolen Emojis", color = discord.Colour.red())
    embed.set_footer(text=f"Emoji: 1/{len(emojis_main)}") 
    embed.set_image(url = url)
    if len(emojis_main) == 1 :
        await ctx.send(embed = embed)
        print(url)
    else:
        await ctx.send(embed = embed, view=fetch_emoji(emojicontent=content_of_mssg))

@bot.hybrid_command(name = "urban", with_app_command = True, description = "Check definiton in urban DIctionary")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def urban(ctx, *msg):

        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        # Send request to the Urban Dictionary API and grab info
        response = requests.get(api, params=[("term", word)]).json()
        embed = discord.Embed(description="No results found!", colour=0xFF0000)
        if len(response["list"]) == 0:
            return await ctx.send(embed=embed)
        # Add results to the embed
        embed = discord.Embed(title="Word", description=word, colour=embed.colour)
        embed.add_field(name="Top definition:", value=response['list'][0]['definition'])
        embed.add_field(name="Examples:", value=response['list'][0]['example'])
        await ctx.send(embed=embed)

@bot.hybrid_command(name = "dm", with_app_command = True, description = "Dm")
@app_commands.guilds(discord.Object(id = 819630334491754547))
@commands.has_permissions(administrator = True)
async def dm(ctx, *, message_and_mentions = None):
    message = None
    mentions = None
    message_and_mentions = message_and_mentions.split(" ")
    message_starting_index = None
    for text_index in range(len(message_and_mentions)):
        if not re.match("\<\@\!?\d*\>|\<\@\&?\d*\>", message_and_mentions[text_index]):
            message_starting_index = text_index
            break
    if message_starting_index is None:
        message_starting_index = len(message_and_mentions)
        message = "This message is sent by " + ctx.author.name
    else:
        message = " ".join(message_and_mentions[message_starting_index:])
    await ctx.defer(ephemeral = True)
    if message_starting_index != 0:
        mentions = []
        for mention in message_and_mentions[:message_starting_index]:
            string_mentions = re.findall("\<\@\!?\d*\>|\<\@\&?\d*\>", mention)
            if string_mentions:
                for mention in string_mentions:
                    print(string_mentions)
                    id = ""; i = 0
                    while i < len(mention):
                        if mention[i].isdigit():
                            id += mention[i]
                        i += 1
                    mentions.append(int(id))
                    await ctx.send("Message Sent!")
        users = []
        for id in mentions:
            user = ctx.message.guild.get_member(id)
            role = ctx.message.guild.get_role(id)
            if user:
                if user not in users:
                    users.append(user)
            elif role:
                for member in ctx.guild.members:
                    if role in member.roles:
                        if member not in users:
                            users.append(member)
        for user in users:
            try:
                await user.send(message)
            except:
                pass
                await ctx.send("Message wasn't sent to a User")


@bot.hybrid_command(name = "advice", with_app_command = True, description = "Get a Random Advice")
@app_commands.guilds(discord.Object(id = 819630334491754547))
@commands.has_permissions(administrator = True)
async def advice(ctx):
    url = "https://api.adviceslip.com/advice"
    r = requests.get(url)
    print(r)
    t = json.dumps(r.json())
    l = json.loads(json.dumps(r.json()))
    print(l)
    lstr = l
    lstr = str(lstr)
    advice = lstr.split(":")[-1]
    advice = advice.replace("}", "")
    embed = discord.Embed(color = 0x2ecc71, title = "Random Advice", description = str(advice))
    await ctx.send(content = None, embed = embed)

@bot.hybrid_command(name = "token", with_app_command = True, description = "tokening")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def token(ctx, member: discord.Member):
    list = ["Blued", "Yellowed"]
    user = ctx.author
    servant = range(1, 60)
    pick = random.choice(servant)
    tokens = random.choice(list)
    print(pick, tokens)
    print(member)
    if user == member :
        await ctx.send(f"Can't token yourself Pleb")

    else:
        await ctx.send (f"{user.mention} {tokens} {member.mention} and defeated {pick} servants")

@bot.hybrid_command(name = "calc", with_app_command = True, description = "calculation")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def calc(ctx, arg):
    y = eval(arg)
    await ctx.defer(ephemeral = True)
    await ctx.send(y)

@bot.hybrid_command(name = "fact", with_app_command = True, description = "Get Random Facts")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def fact(ctx):
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    r = requests.get(url)
    l = json.loads(json.dumps(r.json()))
    fact = (l['text'])
    embed = discord.Embed(color = 0x2ecc71, title = "Random Fact", description = str(fact))
    await ctx.send(content = None, embed = embed)
	

app_id = 'f1b477f2'
app_key = '2fd4ee4cbe6f6751b878c82559aee353'
language = 'en-us'
fields = 'definitions'

word_game = False
@bot.hybrid_command(name = "wordplay", with_app_command = True, description = "WordPlay Game")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def wordplay(ctx):
  global word_game
  if word_game == False:
    word_game = True
    while (word_game==True):
      choose_a_word = random.choice(list_of_word)
      print(choose_a_word)
      lst = [x for x in choose_a_word]
      if len(choose_a_word) <= 3 :
                poppingup = ''.join(random.sample(lst, 1))
                replacing = ''.join(lst)
                hang_word = replacing.replace(poppingup, "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{hang_word}', inline = False)
                await ctx.send(embed = emb)
      elif len(choose_a_word) < 6 :
                poppingup = (random.sample(lst, 2))
                print(poppingup)
                items = choose_a_word.replace(poppingup[0], "#", 1)
                items = items.replace(poppingup[1], "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{items}', inline = False)
                await ctx.send(embed = emb)
      elif len(choose_a_word) < 7 :
                poppingup = (random.sample(lst, 3))
                print(poppingup)
                items = choose_a_word.replace(poppingup[0], "#", 1)
                items = items.replace(poppingup[1], "#", 1)
                items = items.replace(poppingup[2], "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{items}', inline = False)
                await ctx.send(embed = emb)
      elif len(choose_a_word) < 10 :
                poppingup = (random.sample(lst, 4))
                print(poppingup)
                items = choose_a_word.replace(poppingup[0], "#", 1)
                items = items.replace(poppingup[1], "#", 1)
                items = items.replace(poppingup[2], "#", 1)
                items = items.replace(poppingup[3], "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{items}', inline = False)
                await ctx.send(embed = emb)
      elif len(choose_a_word) > 10 :
                poppingup = (random.sample(lst, 5))
                print(poppingup)
                items = choose_a_word.replace(poppingup[0], "#")
                items = items.replace(poppingup[1], "#", 1)
                items = items.replace(poppingup[2], "#", 1)
                items = items.replace(poppingup[3], "#", 1)
                items = items.replace(poppingup[4], "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{items}', inline = False)
                await ctx.send(embed = emb)
      try:
                msg = await bot.wait_for('message', check = lambda x: f"{choose_a_word}" in x.content.lower(), timeout = 10)
                await msg.channel.send(f"{msg.author.mention}, That's correct, The word was **__{choose_a_word.upper()}__**")
      except asyncio.TimeoutError:
            try:
                url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + choose_a_word + "?fields=" + fields
                r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
                t = json.dumps(r.json())
                l = json.loads(json.dumps(r.json()))
                f = l["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
                embed = discord.Embed(color = 0x2ecc71, title = "HINT", description = str(f))
                await ctx.channel.send(content = None, embed = embed)
            except KeyError:
                await ctx.send("**No Hint found in Oxford Dictionary**")
            try:
                 msg = await bot.wait_for('message', check = lambda x: f"{choose_a_word}" in x.content.lower(), timeout = 20)
                 await msg.channel.send(f"{msg.author.mention}, That's correct, The word was **__{choose_a_word.upper()}__**")
            except asyncio.TimeoutError:
                    await ctx.send(f"You're out of time, The word was **__{choose_a_word.upper()}__**")

      if word_game == False:
        pass
      else:
        await ctx.send("Next Question in 10 seconds")
        await asyncio.sleep(10)
  else:
    word_game = False
    await ctx.send("**Word game has stopped**")

word_game = False

@bot.hybrid_command(name = "reminder", with_app_command = True, description = "0h 0m")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def rem(ctx,*, h_m):
 args = h_m
 user = ctx.author
 message = "in".join(args.split("in")[:-1])
 args = args.split(" in ")[-1]
 if "h" in args and "m" in args: 
    main = args.split( )
    print(main)
    x = len(main)
    if x is 2:
        hour = main[0]
        hour_int = hour[:-1]
        minutes = main[1]
        minutes_int = minutes[:-1]
        x1 = int(hour_int)
        x2 = int(minutes_int)
        hour_in_seconds = x1*60*60
        minutes_in_seconds = x2*60
        total_time = hour_in_seconds + minutes_in_seconds
        await ctx.send(f"{user.mention} You'll be reminded for {message} in {args}")
        await asyncio.sleep(total_time)
        await user.send(message)

 elif "h" in args:
    hr = args[:-1]
    hr = int(hr)
    hr_in_seconds = hr*60*60
    await ctx.send(f"{user.mention} You'll be reminded for {message} in {args}")
    await asyncio.sleep(hr_in_seconds)
    await user.send(message)

 elif "m" in args:
    min = args[:-1]
    min = int(min)
    min_in_seconds = min*60
    await ctx.send(f"{user.mention} You'll be reminded for {message} in {args}")
    await asyncio.sleep(min_in_seconds)
    await user.send(message)

 else:
    await ctx.send("Use Correct Format: Pls rem (message) in (0)h (0)m")

@bot.hybrid_command(name = "avatar", with_app_command = True, description = "Check avatar of a Guild Member")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def avatar(ctx, *, member: discord.Member=None):
    if not member: 
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@bot.command()
async def say(ctx, *, text):
    if ctx.message.author.id == 705116051024773213:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")
    elif ctx.message.author.id == 856036736970260490:
        await ctx.send(f"{ctx.message.author.mention} You're yet to inherit me")
    elif text == "Only Tam is allowed to use it noob.":
        await ctx.send(f"{ctx.message.author.mention} stfu")
    else:
        await ctx.send('Only Tam is allowed to use it noob.')

@bot.command()
async def say(ctx, *, text):
    if ctx.message.author.id == 705116051024773213:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")
    elif ctx.message.author.id == 856036736970260490:
        await ctx.send(f"{ctx.message.author.mention} You're yet to inherit me")
    elif text == "Only Tam is allowed to use it noob.":
        await ctx.send(f"{ctx.message.author.mention} stfu")
    else:
        await ctx.send('Only Tam is allowed to use it noob.')

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle, activity=discord.Game('with OwO'))
 
@bot.hybrid_command(name = "translate", with_app_command = True, description = "Translate any message to english", aliases =["ts"])
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def translate(ctx, *, inptext = None):
    translator = Translator()
    translated_text = translator.translate(inptext)
    embed = discord.Embed(title="Translate", description = translated_text.text)
    embed.set_footer(text=f"Source Langauge : '{translated_text.src}'")
    await ctx.send(embed = embed)     



@bot.hybrid_command(name = "steal", with_app_command = True, description = "Steal other's Luck")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def steal(ctx,*, member: discord.Member):
    list1 = f"{ctx.author.mention} tried to steal {member.mention}'s luck but failed"
    list2 = f"{ctx.author.mention} stole {member.mention}'s Good luck"
    list22 = f"{ctx.author.mention} stole {member.mention}'s Bad luck"
    list3 = f"{ctx.author.mention} stole {member.mention}'s luck, Not sure Good or Bad"
    lists = [list1, list2, list3, list22]
    choose = random.choice(lists)
    if member is ctx.author :
        await ctx.send("No need to steal your own luck noob")
    elif ctx.author is 705116051024773213 :
        await ctx.send(f"Can't steal Creator's Luck")
    else:
      await ctx.send(choose)

@bot.event
async def on_message_delete(message):
    global deleted_messages
    deleted_messages[message.channel.id] = {'author': message.author.name+'#'+message.author.discriminator, 'content': message.content, 'avatar_url': message.author.avatar_url}

@bot.hybrid_command(name = "snipe", with_app_command = True, description = "Snipe last deleted message")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def snipe(ctx):
    global deleted_messages
    if ctx.message.channel.id in deleted_messages:
        embed=discord.Embed(title="",description=f"{deleted_messages[ctx.message.channel.id]['content']}")    
        embed.set_author(name="Sniper", icon_url=deleted_messages[ctx.message.channel.id]['avatar_url'])
        embed.set_footer(text=f"Message deleted by {deleted_messages[ctx.message.channel.id]['author']}")
    else:
        embed=discord.Embed(title="Sniper",description="Nothing to snipe!")
    await ctx.send(embed = embed)

old = {}
new = {}
author = {}

deleted_messages = {}

@bot.event
async def on_message_edit(before, after):
    global old
    global new
    global author 
    old[before.channel.id] = before.content
    new[after.channel.id] = after.content
    author[after.channel.id] = after.author.name

@bot.hybrid_command(name = "snipe_edit", with_app_command = True, description = "Snipe last edited message")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def snipeedit(ctx):
    if ctx.message.channel.id in new:
        embed=discord.Embed(title="",description=f"Before: {old[ctx.message.channel.id]}\nAfter: {new[ctx.message.channel.id]}")    
        #embed.set_author(name="Sniper", icon_url={after.author.avatar_url})
        embed.set_footer(text=f"Message edited by {author[ctx.message.channel.id]}")       
    else:
        embed=discord.Embed(title="Sniper",description="No Edit to snipe!")
    await ctx.send(embed=embed)

@bot.hybrid_command(name = "define", with_app_command = True, description = "Get definition of a Word")
@app_commands.guilds(discord.Object(id = 819630334491754547))
async def define(ctx, word):
    words = word
    print(words)
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + words.lower() + "?fields=" + fields
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
    t = json.dumps(r.json())
    l = json.loads(json.dumps(r.json()))
    f = l["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    embed = discord.Embed(colour = discord.Colour.from_rgb(107, 230, 255), title = 'Oxford Dictionary - ' + word, description = str(f))
    await ctx.send(content = None, embed = embed)

print("Bot is Online")
bot.run(os.getenv('TOKEN'))
