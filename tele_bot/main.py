import datetime
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import telebot
import random

load_dotenv()
KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(KEY)

sosy = ('jalapeno', '1000 wysp', 'firecracker', 'algierski', 'musztarda bbq', 'bbq', 'slodkie chili', 'amerykanski',
        'serowy', 'paprykowy sriracha', 'arabski', 'curry&mango', 'czosnkowy', 'ketchup', 'musztarda', 'remoulada',
        'andaluzyjski', 'meksykanski')


@bot.message_handler(commands=['sosiwo'])
def sosiwo(message):
    bot.reply_to(message, random.choice(sosy))


@bot.message_handler(commands=['sosy'])
def sosiwo(message):
    bot.reply_to(message, random.choice(sosy) + " " + random.choice(sosy))


@bot.message_handler(commands=['hlanie'])
def picie(message):
    decyzja = ['tak', 'nie']
    name = message.from_user.first_name
    if name == 'Michał':
        bot.reply_to(message, "Dla pana michała nie ma picia")
    else:
        bot.reply_to(message, random.choice(decyzja))


@bot.message_handler(commands=['gp'])
def gp(message):
    timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    gp = "2021-10-24 21:00:00"
    start = datetime.datetime.strptime(timenow, '%Y-%m-%d %H:%M:%S')
    ends = datetime.datetime.strptime(gp, '%Y-%m-%d %H:%M:%S')
    result = ends - start
    minuty = (result.seconds - (result.seconds // 3600) * 3600) // 60
    if (result.days > 7):
        bot.reply_to(message, "no rawe ceek  this time")
    elif (result.days <= 7):
        bot.reply_to(message, "Do grand prix zostało " + str(result.days) + " dni, oraz " + str(
            result.seconds // 3600) + " godzin i " + str(minuty) + " minuty")


@bot.message_handler(commands=['promocja'])
def zabka(message):
    url = 'https://www.zabka.pl/produkty/szukaj-piwa-po-kolorze-polki'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    lista = soup.find_all('div', class_='grid__col -auto-height -col-sm-6 -col-md-4 -col-xl-3')
    piwa = []
    quote = {}
    for x in lista:
        quote['alkohol'] = x.img['alt']
        quote['cena'] = (x.select_one("span.price.product__price").text[9]) + "." + (
            x.select_one("span.price.product__price").text[10:12])
        quote['sztuki'] = x.select_one("span.badge__name").text[26]
        piwa.append(quote.copy())

    bot.send_message(message.chat.id, str(piwa))


bot.polling()
