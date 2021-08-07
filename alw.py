import discord
from discord.ext import commands
import time

token = "ODU1MDkzOTEwMzAzNjcwMzAz.YMteQw.NymDbkb7M3PePzAt4r-BbGzK7r8"

bot = commands.Bot(command_prefix = '*')
@bot.command()
async def test(ctx):
    await ctx.send("i heard it my son! {}".format(ctx.author))

@bot.command()
async def c(ctx):
    for i in range(1,61,10):
        j = "The Wait over is : "+str(i) + " seconds"
        await ctx.send(j,delete_after = 2)
        time.sleep(9.7)


@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send("ok")

@bot.command()
async def leave(ctx):
    ch = ctx.guild.voice_client
    await ch.disconnect()


bot.run(token)
