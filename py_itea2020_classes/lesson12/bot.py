from config import TOKEN
from telebot import TeleBot
import time
import random
from telebot.types import  KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import json

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    print(message)
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = KeyboardButton('Hello', request_contact=True)
    button2 = KeyboardButton('Hi', request_location=True)
    button3 = KeyboardButton('Hola')

    kb.add(button1, button2, button3)

    bot.send_message(message.chat.id, 'Hello!', reply_markup=kb)


@bot.message_handler(func=lambda m: m.text in {'Hi', 'Hello', 'Hola'})
def handle_hello(message):
    greetings = ['Hola', 'Hello', 'Hi']

    kb = InlineKeyboardMarkup()
    json_data = json.dumps({'tag': 'Greeting',
                            'id': '1234'})
    #button1 = InlineKeyboardButton('Hello', callback_data='1234')
    button1 = InlineKeyboardButton('Hello', callback_data=json_data)

    json_data = json.dumps({'tag': 'Goodbye',
                            'id': '5678'})
    #button2 = InlineKeyboardButton('Hello google', url='https://google.com')
    button2 = InlineKeyboardButton('Goodbye', callback_data=json_data)
    kb.add(button1, button2)

    bot.send_message(message.chat.id, random.choice(greetings), reply_markup=kb)


#@bot.callback_query_handler(func=lambda c: True)
@bot.callback_query_handler(func=lambda c: json.loads(c.data).get('tag') == 'Greeting')
def handle_inline(call):
    print(call)
    bot.send_message(call.message.chat.id, 'Hiiiiiii')


@bot.callback_query_handler(func=lambda c: json.loads(c.data).get('tag') == 'Goodbye')
def handle_inline(call):
    print(call)
    bot.send_message(call.message.chat.id, 'Byeeeee')


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
