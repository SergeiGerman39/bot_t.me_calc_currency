import requests
import telebot
import json

from config import *


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Калькулятор валюты \n' \
           ' Для начала работы введите информацию \n в следующем порядке: \n 1. Трёхзначный код валюты: \n рубли (RUB), доллары (USD), Евро (EUR), Польский злотый (PLN). \n' \
           '2. Трёхзначный код валюты в которую хотите перевести:\n рубли (RUB), доллары (USD), Евро (EUR), Польский злотый (PLN). \n' \
           '3. Количество переводимой валюты.' \
           'Увидеть список всех доступных валют - команда /currency'
    bot.reply_to(message, text)


@bot.message_handler(commands=['currency'])
def currency(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in currencies.keys():
        text = '\n'.join((text, key,))

    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    base_key, to_key, amount = message.text.split()
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={to_key}&base={base_key}"

    payload = {}
    headers = {
        "apikey": "0D6jarTZtAIl4gzf5sG00nW9lQt4Wz5a"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp = json.loads(response.content)
    new_amount = resp['rates'][to_key] * float(amount)
    bot.reply_to(message, f'Сумма {amount} {base_key} в {to_key}: {new_amount}')


bot.polling()
