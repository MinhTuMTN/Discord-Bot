import discord
import thptqg_scores as thptqg
import os

TOKEN = os.getenv('token')

# Tạo client bot
client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello, I am your Discord bot!')
    elif message.content.startswith('!thptqg'):
        identificationNumber = message.content.split(' ')[1]
        scores = thptqg.scoreLookup(identificationNumber)

        text = 'Số báo danh không hợp lệ hoặc không thể tìm thấy kết quả'
        if (scores != None):
            text = scores

        await message.reply(content=text)

client.run(TOKEN)
