# from telebot.async_telebot import AsyncTeleBot
# import asyncio
import aiohttp
import requests
import csv
import telebot
from telebot import types
from random import randint
from CSV_Writer import find_by

bot = telebot.TeleBot('6362766998:AAHxpOOKZXpHkaSa1tbJbVJ4C3SwJwyThZg')
COIN_NAME_TO_FIND = ""  # Creating the global variable for coinName


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Test Test Test"
                                      "This bot will write data about your car into CSV file")
    back(message)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'choose' or call.data == 'back':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        write = types.KeyboardButton('Write')
        read = types.KeyboardButton('Read')
        filterCars = types.KeyboardButton('Filter')
        markup_reply.add(write, read, filterCars)
        bot.send_message(call.message.chat.id, 'Choose ', reply_markup=markup_reply)
    # elif call.data == 'filterByMake':
    #     await bot.send_message(call.message.chat.id, 'Enter the make of a car')
    #     await bot.reply_to()


@bot.message_handler(content_types=['text'])
def send_price(message):
    if message.text == 'Write':
        bot.send_message(message.chat.id,
                         """Enter data about car. Copy next message and provide data next to the naming.""")
        bot.send_message(message.chat.id, f"""{message.chat.id}:
Make: Toyota
Model: Highlander
Year: 2021
Price: 45000
Milage: 32000""")

        # await bot.send_message(message.chat.id, f"""Курсы валют на
        #     - Binance \"BUY\"
        #     {binance_buy_rate}
        #     - Binance \"SELL\"
        #     {binance_sell_rate}""")
    elif message.text == 'Car for test':
        bot.send_message(message.chat.id, message.text.split()[0])
    elif message.text == 'Read':
        reading(message)
    elif message.text.split(":")[0] == str(message.chat.id):
        messageArr = message.text.split()
        writing(messageArr, message)
        reading(message)
    elif message.text == 'Filter':
        # markup_inline = types.InlineKeyboardMarkup()
        # filterMake = types.InlineKeyboardButton(text='Filter Make', callback_data='filterByMake')
        # filterModel = types.InlineKeyboardButton(text='Filter Model', callback_data='filterByModel')
        # markup_inline.add(filterMake)
        # markup_inline.add(filterModel)
        # await bot.send_message(message.chat.id, 'Choose an option:', reply_markup=markup_inline)

        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        choosingMake = types.KeyboardButton('Make')
        choosingModel = types.KeyboardButton('Model')
        backup = types.KeyboardButton('back')
        # choosing = types.InlineKeyboardButton(text='Choose', callback_data='choose')
        markup_reply.add(choosingMake, choosingModel, backup)
        bot.send_message(message.chat.id, 'Choose filter type:', reply_markup=markup_reply)

    elif message.text == 'sexy':
        bot.send_message(message.chat.id, f"""Ты тоже сладкий 👨‍❤️‍👨""")
    elif message.text == 'BTS':
        pic = 'https://sun9-75.userapi.com/impg/c857524/v857524361/111459/0xxLNZq9ieU.jpg?size=1280x720&quality=96&sign=200c85a227cf6387c9c6f1f0b145f0eb&c_uniq_tag=rDbKMxvSTPa1Kz8ddtMtaSCLuPWv_bTd1cwzNsDkEyw&type=album'
        bot.send_photo(message.chat.id, pic)
        # await bot.send_message(message.chat.id, f"""Не братан, мы пидорасню не слушаем""")
    elif message.text == 'back':
        back(message)
    elif message.text == 'Make':
        msgMake = bot.send_message(message.chat.id, 'What is a car make?')
        bot.register_next_step_handler(msgMake, a_handler)
    elif message.text == 'Model':
        msgModel = bot.send_message(message.chat.id, 'What is a car model?')
        bot.register_next_step_handler(msgModel, b_handler)
# @bot.callback_query_handler(func=lambda call: True)
# def filters(call):
#     if call.data == 'make':
#         msg = bot.send_message(call.message.chat.id, 'What is the car make?')
#         bot.register_next_step_handler(msg, a_handler)
#     elif call.data == 'model':
#         msg = bot.send_message(call.message.chat.id, 'What is the car model?')
#         bot.register_next_step_handler(msg, b_handler)


def writing(messageArr, message):
    carData = [[messageArr[2], messageArr[4], messageArr[6], messageArr[8], messageArr[10], ]]
    with open("MOCK_DATA.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerows(
            carData
        )
    bot.send_message(message.chat.id, messageArr)


def a_handler(message):
    token = randint(0, 1000000)
    maketmp = message.text
    find_by(maketmp, token, 'Make')
    bot.send_document(message.chat.id, open(f'FilterByMakeTests/{maketmp}-{token}.csv', 'rb'))

def b_handler(message):
    token = randint(0, 1000000)
    modeltmp = message.text
    find_by(modeltmp, token, 'Model')
    bot.send_document(message.chat.id, open(f'FilterByModelTests/{modeltmp}-{token}.csv', 'rb'))

def reading(message):
    bot.send_document(message.chat.id, open(r'MOCK_DATA.csv', 'rb'))

def back(message):
    markup_inline = types.InlineKeyboardMarkup()
    choosing_coin = types.InlineKeyboardButton(text='Choose', callback_data='choose')
    markup_inline.add(choosing_coin)
    bot.send_message(message.chat.id, 'Choose an option:', reply_markup=markup_inline)
bot.infinity_polling()

# if __name__ == '__main__':
#     telebot.run(bot.polling())
