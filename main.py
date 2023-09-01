from telebot.async_telebot import AsyncTeleBot
import asyncio
import aiohttp
import requests
import csv
from telebot import types

from CSV_Writer import find_by_make

bot = AsyncTeleBot('6362766998:AAHxpOOKZXpHkaSa1tbJbVJ4C3SwJwyThZg')
COIN_NAME_TO_FIND = ""  # Creating the global variable for coinName

@bot.message_handler(commands=['start'])
async def start_message(message):
    await bot.send_message(message.chat.id, "Test Test Test"
                                            "This bot will write data about your car into CSV file")
    markup_inline = types.InlineKeyboardMarkup()
    choosing_coin = types.InlineKeyboardButton(text='Choose', callback_data='choose')
    markup_inline.add(choosing_coin)
    await bot.send_message(message.chat.id, 'Choose an option:', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
async def answer(call):
    if call.data == 'choose':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        write = types.KeyboardButton('Write')
        read = types.KeyboardButton('Read')
        filterCars = types.KeyboardButton('Filter')
        markup_reply.add(write, read, filterCars)
        await bot.send_message(call.message.chat.id, 'Choose ', reply_markup=markup_reply)
    # elif call.data == 'filterByMake':
    #     await bot.send_message(call.message.chat.id, 'Enter the make of a car')
    #     await bot.reply_to()


@bot.message_handler(content_types=['text'])
async def send_price(message):

    if message.text == 'Write':
        await bot.send_message(message.chat.id,
                               """Enter data about car. Copy next message and provide data next to the naming.""")
        await bot.send_message(message.chat.id, f"""{message.chat.id}:
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
        await bot.send_message(message.chat.id, message.text.split()[0])
    elif message.text == 'Read':
        await reading(message)
    elif message.text.split(":")[0] == str(message.chat.id):
        messageArr = message.text.split()
        await writing(messageArr, message)
        await reading(message)
    elif message.text == 'Filter':
        # markup_inline = types.InlineKeyboardMarkup()
        # filterMake = types.InlineKeyboardButton(text='Filter Make', callback_data='filterByMake')
        # filterModel = types.InlineKeyboardButton(text='Filter Model', callback_data='filterByModel')
        # markup_inline.add(filterMake)
        # markup_inline.add(filterModel)
        # await bot.send_message(message.chat.id, 'Choose an option:', reply_markup=markup_inline)
        await bot.reply_to(message, 'What is the car make?')
        await bot.register_next_step_handler()
    elif message.text == 'sexy':
        await bot.send_message(message.chat.id, f"""Ты тоже сладкий 👨‍❤️‍👨""")
    elif message.text == 'BTS':
        pic = 'https://sun9-75.userapi.com/impg/c857524/v857524361/111459/0xxLNZq9ieU.jpg?size=1280x720&quality=96&sign=200c85a227cf6387c9c6f1f0b145f0eb&c_uniq_tag=rDbKMxvSTPa1Kz8ddtMtaSCLuPWv_bTd1cwzNsDkEyw&type=album'
        await bot.send_photo(message.chat.id, pic)
        # await bot.send_message(message.chat.id, f"""Не братан, мы пидорасню не слушаем""")


async def writing(messageArr, message):
    carData = [[messageArr[2], messageArr[4], messageArr[6], messageArr[8], messageArr[10], ]]
    with open("data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerows(
            carData
        )
    await bot.send_message(message.chat.id, messageArr)


async def reading(message):
    await bot.send_document(message.chat.id, open(r'data.csv', 'rb'))


if __name__ == '__main__':
    asyncio.run(bot.polling())
