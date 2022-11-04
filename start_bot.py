import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(config("TOKEN_BOT"))


@bot.message_handler(commands=["start", "hi"])
def get_start_message(message):
    full_name = f"{message.from_user.username}"
    text = f"Welcome {full_name}"
    bot.send_message(message.chat.id, text)
    # bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def get_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if message.text.lower() == "меню":
        text = "Выберите пожалуйста: чай или кофе"
        btn1 = types.InlineKeyboardButton("Чай", callback_data="tea")
        btn2 = types.InlineKeyboardButton("Кофе", callback_data="coffee")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def get_callback_data(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if call.data == "tea":
        btn1 = types.KeyboardButton("black tea")
        btn2 = types.KeyboardButton("blue tea")
        btn3 = types.KeyboardButton("green tea")
        markup.add(btn1, btn2, btn3)
    if call.data == "coffee":
        btn1 = types.KeyboardButton("latte")
        btn2 = types.KeyboardButton("Cappucciano")
        btn3 = types.KeyboardButton("Espresso")
        markup.add(btn1, btn2, btn3)
    bot.send_message(call.message.chat.id, f"Would you rather to drink", reply_markup=markup)




bot.polling()