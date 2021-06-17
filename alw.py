import discord
from discord.ext import commands

token = "ODU1MDkzOTEwMzAzNjcwMzAz.YMteQw.NymDbkb7M3PePzAt4r-BbGzK7r8"

bot = commands.Bot(command_prefix = '*')
@bot.command()
async def test(ctx):
    await ctx.send("i heard it my son! {}".format(ctx.author))


@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    ch = ctx.guild.voice_client
    await ch.disconnect()


bot.run(token)
