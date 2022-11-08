import telebot
from decouple import config
from telebot import types
import random
import string


bot = telebot.TeleBot(config("TOKEN_BOT"))





length = 10
length1 = 20

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, length)
temp1 = random.sample(all, length1)
password = "".join(temp)
password1 = "".join(temp1)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Русский")
    btn2 = types.KeyboardButton("English")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Пожалуйста выберите язык | Please choose your language".format(message.from_user), reply_markup=markup)

# ВЫБОР ЯЗЫКА
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Русский"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        text = "Какой пароль хотите: Простой или Сложный?"
        btn1 = types.KeyboardButton("Простой")
        btn2 = types.KeyboardButton("Сложный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text, reply_markup=markup)
    elif(message.text == "English"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        text = "What kind of password do you want: Easy or Strong?"
        btn1 = types.KeyboardButton("Easy")
        btn2 = types.KeyboardButton("Strong")
        back = types.KeyboardButton("Back to main menu")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text, reply_markup=markup)
# ГЕНЕРАЦИЯ ПАРОЛЯ
    elif (message.text == "Простой"):
        bot.send_message(message.chat.id, f' You password:  {"".join(random.sample(all, length))}')

    elif (message.text == "Сложный"):
        bot.send_message(message.chat.id, f' Ваш пароль:  {"".join(random.sample(all, length1))}')

    elif (message.text == "Easy"):
        bot.send_message(message.chat.id, f' You password:  {"".join(random.sample(all, length))}')

    elif (message.text == "Strong"):
        bot.send_message(message.chat.id, f' You password:  {"".join(random.sample(all, length1))}')

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Русский")
        button2 = types.KeyboardButton("English")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "Back to main menu"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Русский")
        button2 = types.KeyboardButton("English")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="You came back to main menu", reply_markup=markup)



bot.polling()


