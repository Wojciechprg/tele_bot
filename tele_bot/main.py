import os
import telebot
import random
#API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot('2038787201:AAFnwe7TcHfEMEp3Jdyy4I0HQY5gFG_aeJQ')


@bot.message_handler(commands=['sosiwo'])
def sosiwo(message):
    sosy = ['jalapeno', '1000 wysp', 'firecracker', 'algierski', 'musztarda bbq', 'bbq', 'slodkie chili', 'amerykanski',
            'serowy', 'paprykowy sriracha', 'arabski', 'curry&mango', 'czosnkowy', 'ketchup', 'musztarda', 'remoulada',
            'andaluzyjski', 'meksykanski']

    bot.reply_to(message, random.choice(sosy))

@bot.message_handler(commands=['sosy'])
def sosiwo(message):
    sosy = ['jalapeno', '1000 wysp', 'firecracker', 'algierski', 'musztarda bbq', 'bbq', 'slodkie chili', 'amerykanski',
            'serowy', 'paprykowy sriracha', 'arabski', 'curry&mango', 'czosnkowy', 'ketchup', 'musztarda', 'remoulada',
            'andaluzyjski', 'meksykanski']

    bot.reply_to(message, random.choice(sosy)+" "+ random.choice(sosy))

@bot.message_handler(commands=['hlanie'])
def picie(message):
    decyzja = ['tak', 'nie']
    bot.reply_to(message, random.choice(decyzja))

bot.polling()
