import discord
import os
from discord import FFmpegPCMAudio
from discord.ext import commands
import random

bot_token = os.environ['BOT_TOKEN']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


async def on_ready():
    print(f'logged as {bot.user}\t{bot.user.id}')


@bot.command(pass_context=True)
async def lobster(ctx):

    if random.randint(1, 10) == 1:
        await ctx.send("Chingas a tu madre, no quiero.")
        return

    channel = ctx.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio("lobster.mp3")
    voice.play(source)


@bot.command(pass_context=True)
async def leave_lobster(ctx):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Adios Judios")


bot.run(bot_token)
