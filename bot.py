import source
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Moex")
    btn2 = types.KeyboardButton("Steam")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Начало работы", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Moex':
        ans = source.getMoex()
        bot.send_message(message.chat.id, ans)
    elif message.text == 'Steam':
        ans = source.getSteam()
        bot.send_message(message.chat.id, ans)


bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
