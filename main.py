import discord
import os
from discord import FFmpegPCMAudio
from discord.ext import commands
import random
import youtube_dl

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

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=BCjzPXtIh_c'])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            os.rename(file, 'lobster.mp3')

    source = FFmpegPCMAudio("lobster.mp3")
    voice.play(source)


@bot.command(pass_context=True)
async def leave_lobster(ctx):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Adios Judios")


bot.run(bot_token)
