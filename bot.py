import telebot
import time

bot_token = '1196417323:AAGBq8M9bWIxKynf9lwMiC_dT8_ZEmeBzq4'

bot = telebot.Telebot(token=bot_token)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'welcome!')
    
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'to use t his bot,send it a username')
    
@bot.message_handler(func=lambda msg: msg.text is not None and '@'is in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))
    

while true:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
  
