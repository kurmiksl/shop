import telebot
from decouple import config

token = config("TOKEN")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEIBUNkBXZrFzZ0XSpsTt2qC-RU22CXOAACRwADUomRI9gLnctNAkcNLgQ")
    bot.send_photo(message.chat.id, 'https://images.app.goo.gl/58p9aQw2egar3Rqe6')

@bot.message_handler(content_types=['text'])
def aaaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    else:
        bot.send_message(message.chat.id, 'Сообщение не распознанно')    

@bot.message_handler(content_types=['sticker'])
def bbbb(message): 
    bot.send_sticker(message.chat.id, message.sticker .file.id)
    bot.send_message(message.chat.id, message.sticker .file.id)

bot.polling()

