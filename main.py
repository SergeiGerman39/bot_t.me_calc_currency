import telebot

from config import *
from extensions import Convertor, APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Калькулятор валюты \n' \
           ' Для начала работы введите информацию \n в следующем порядке: \n ' \
           '1. Наименование валюты которую хотите перевести. \n' \
           '2. Валюта в которую хотите перевести. \n' \
           '3. Количество переводимой валюты.' \
           'Увидеть список всех доступных валют - команда /currency'
    bot.reply_to(message, text)


@bot.message_handler(commands=['currency'])
def currency(message: telebot.types.Message):
    text = 'Доступные для конвертации валюты:'
    for key in currencies.keys():
        text = '\n'.join((text, key,))

    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        base_key, to_key, amount = message.text.split()
    except ValueError as e:
        bot.reply_to(message, "Вы ввели не верное количество параметров!")

    try:
        new_amount = Convertor.get_price(base_key, to_key, amount)
        bot.reply_to(message, f'Сумма {amount} {base_key} в {to_key}: {new_amount}')
    except APIException as e:
        bot.reply_to(message, f"Ошибка в запросе: \n{e}")


bot.polling()
