from config import TOKEN
from telebot import TeleBot
import time
import random

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    print(message)
    bot.send_message(message.chat.id, 'Hello!')

@bot.message_handler(func=lambda m: m.text == 'Hi')
def handle_hello(message):
    greetings=['Hola', 'Hello', 'Hi']
    bot.send_message(message.chat.id, random.choice(greetings))

#
# @bot.message_handler(commands=['whoami'])
# def handle_whoami(message):
#     print(message)
#     user_info = f'Your name is {message.from_user.id}\n'\
#                 f'Login: @{message.from_user.username}'
#     bot.send_message(message.chat.id, user_info)
#
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'You wrote me '+ message.text)

# for i in range(3):
#     bot.send_message(794857798, 'Hiiiii')
#     time.sleep(0.5)

bot.polling()
