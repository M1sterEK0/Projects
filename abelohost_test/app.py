import discord
from discord.ext import commands
import json
from config import settings


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents, help_command=None)


                                                #JSON

try:
    with open('users.json') as fp:
        users = json.load(fp)
except Exception:
    users = {}


def save_users():
    with open('users.json', 'w+') as fp:
        json.dump(users, fp, sort_keys=True, indent=4)


def add_points(user: discord.User, points: int):
    id = user.id
    if id not in users:
        users[id] = {}
    users[id]['Messages'] = users[id].get('Messages', 0) + points
    
    if users[id].get("Messages", 0) // 20 < 1:
        users[id]['Level'] = 1
    else:
        users[id]['Level'] = users[id].get('Messages', 0) // 20
    
    save_users()


def get_level(user: discord.User):
    id = user.id
    if id in users:
        return users[id]['Level']
    return 1


                                                #EVENTS

@client.event
async def on_ready():
    print(f'We have logged in as {client}')
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('.'):
        await client.process_commands(message)
    
    else:
        add_points(message.author, 1)

    

@client.event
async def on_member_join(member):
    guild = member.guild
    channel = client.get_channel(892394255090335846)
    await member.send(f'Welcome to {guild}')
    await channel.send(f'New user {member.name} is connected!')
    print(f'Connect new user {member.name}')


                                                #COMMANDS

@client.command() # Знаю, что процедура создания команды Help - по умолчанию другая, сделал так потому, что просто меньше кода. 
async def help(ctx):
    await ctx.send('''Это .help-справка по командам бота.\n.kick [имя пользователя] - выгнать пользователя\n.ban [имя пользователя] - забанить пользователя\n\
.uban [имя пользователя] - разбанить пользователя\n.lvl - узнать свой уровень\n.kuzya - расслабиться как мой кот''')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):

    if member.guild_permissions.administrator:
        await ctx.channel.send(f'Hi {ctx.author.name}! It is impossible to ban administrators.')

    else:
        if reason is None:
            await member.send(f'Hi {member.name}! You have been banned from {ctx.channel.guild.name}. You must have done something wrong. VERY BAD!')
            await ctx.channel.send(f'Hi {ctx.author.name}! {member.name} has been banner succesfully from this server!')
            await member.ban()
        
        else: 
            await member.send(f'Hi {member.name}! You have been banned from {ctx.channel.guild.name}. You must have done something wrong. VERY BAD! :angry: :triumph: \n \nReason: {reason}')
            await ctx.channel.send(f'Hi {ctx.author.name}! {member.name} has been banner succesfully from this server! \n\n Reason: {reason}')
            await member.ban()


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
  
    for ban_entry in banned_users:
        user = ban_entry.user
  
    if user.name == member:
        await ctx.guild.unban(user)
        await ctx.send(f"{user} have been unbanned sucessfully")
        return


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f"{member} have been kicked sucessfully")


@client.command()
async def lvl(ctx):
    await ctx.send(f'You lvl is {get_level(ctx.author)}')


@client.command()
async def kuzya(ctx):
    await ctx.send(file=discord.File('.\src\kuzya.jpg'))


client.run(settings['token'])


