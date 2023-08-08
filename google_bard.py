import os
from Bard import Chatbot


def askBard(question):
    chatbot = Chatbot(os.getenv('bard_token'))
    return chatbot.ask(question)['content']
