import os
import telebot
import random
import datetime
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
    name = message.from_user.first_name
    if name == 'Michał':
     bot.reply_to(message, "Dla pana michała nie ma picia")
    else:
     bot.reply_to(message, random.choice(decyzja))

@bot.message_handler(commands=['gp'])
def gp(message):
    timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    gp = "2021-10-10 15:00:00"
    start = datetime.datetime.strptime(timenow, '%Y-%m-%d %H:%M:%S')
    ends = datetime.datetime.strptime(gp, '%Y-%m-%d %H:%M:%S')
    result = ends - start
    minuty = (result.seconds - (result.seconds // 3600) * 3600) // 60
    if (result.days > 7):
        bot.reply_to(message,"no rawe ceek  this time")
    elif (result.days <= 7):
        bot.reply_to(message,"Do grand prix zostało " + str(result.days) + " dni, oraz " + str(
            result.seconds // 3600) + " godzin i " + str(minuty) + " minuty")

bot.polling()
