# -*- coding: utf-8 -*-

import telebot
import requests
import json
import string
from random import *

min_char = 4
max_char = 5

API_TOKEN = '<PLACE_YOUR_FATHER_BOT_TOKEN>'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "To start send /short <link>")

@bot.message_handler(commands=['short'])
def short(m):
    chat = m.text[9:]
    if chat == "":
        bot.send_message(m.chat.id, "You need to send /short <link>")
    else:

        link = m.text.split()[1] 
        allchar = string.ascii_letters + string.digits
        randomWord = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
        url = 'https://<PLACE_YOUR_YOURLS_DOMAIN>/yourls-api.php?signature=<PLACE_YOUR_SIGNATURE>&action=shorturl&url=' + link + '&keyword=' + randomWord + '&format=json'

        try:
            r = requests.get(url)
            res = r.json()
            if res["statusCode"] == 200:
                bot.send_message(m.chat.id, "*Here it is*", parse_mode='Markdown')
                bot.send_message(m.chat.id, str(res["shorturl"]), disable_web_page_preview=True)
            else:
                bot.send_message(m.chat.id, "Error: _"+str(message)+"_", parse_mode='Markdown')
        except:
            bot.send_message(m.chat.id, "An error occurred sending http request.")
bot.polling(none_stop=True, timeout=9999999)
