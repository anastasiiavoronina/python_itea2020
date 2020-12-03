from config import TOKEN
from telebot import TeleBot
from user_info_model import UserInfo

bot = TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    print(message)
    bot.send_message(message.chat.id, 'Please provide your full name')
    users[message.chat.id] = {'fio'        : None,
                              'phone'      : None,
                              'email'      : None,
                              'address'    : None,
                              'suggestions': None,
                              'id_in_db'   : None}
    print(users)

@bot.message_handler(content_types=['text'])
def handle_hello(message):
    if message.chat.id in users:
        text = message.text
        if users[message.chat.id]['fio'] == None:
            users[message.chat.id]['fio'] = text
            ui = UserInfo(fio=text)
            ui.save()
            print(ui.id)
            users[message.chat.id]['id_in_db'] = ui.id
            bot.send_message(message.chat.id, 'Please provide your phone')
        elif users[message.chat.id]['phone'] == None:
            ui = UserInfo.objects().get(id=users[message.chat.id]['id_in_db'])
            ui.update(phone=text)
            users[message.chat.id]['phone'] = text
            bot.send_message(message.chat.id, 'Please provide your email')
        elif users[message.chat.id]['email'] == None:
            ui = UserInfo.objects().get(id=users[message.chat.id]['id_in_db'])
            ui.update(email=text)
            users[message.chat.id]['email'] = text
            bot.send_message(message.chat.id, 'Please provide your address')
        elif users[message.chat.id]['address'] == None:
            ui = UserInfo.objects().get(id=users[message.chat.id]['id_in_db'])
            ui.update(address=text)
            users[message.chat.id]['address'] = text
            bot.send_message(message.chat.id, 'Please provide your suggestions')
        elif users[message.chat.id]['suggestions'] == None:
            ui = UserInfo.objects().get(id=users[message.chat.id]['id_in_db'])
            ui.update(suggestions=text)
            users[message.chat.id]['suggestions'] = text
            bot.send_message(message.chat.id, 'Now survey is over')
        else:
            bot.send_message(message.chat.id, 'You have already provided all required information. '\
                                              'If you want to start from the beginning please use command "/start"')
    else:
        bot.send_message(message.chat.id, 'If you want to provide information about you please use command "/start"')

bot.polling()
