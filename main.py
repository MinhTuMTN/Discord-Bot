import discord
import thptqg_scores as thptqg
import os
from Bard import AsyncChatbot

TOKEN = os.getenv('token')

# Tạo client bot
client = discord.Client(intents=discord.Intents.all())

token_1 = os.getenv('bard_cookie_1')
token_2 = os.getenv('bard_cookie_2')
chatbot = None


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
  global chatbot

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
  elif message.content.startswith('!bard'):
    if chatbot == None:
      chatbot = await AsyncChatbot.create(token_1, token_2)

    question = ' '.join(message.content.split(' ')[1:])
    response = await chatbot.ask(question)

    await message.reply(content=response['content'])


client.run(TOKEN)
