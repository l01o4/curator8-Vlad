import telebot

bot = telebot.TeleBot('6452231526:AAErmCm-GeKlOphh-Azo4-YRmLfeTtgbQlw')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'МОТИВАЦИЯ ДОЛЖНА БЫТЬ ВСЕГДА!')


@bot.message_handler(commands=['motivation'])
def main(message):
    bot.send_message(message.chat.id, 'МОТИВАЦИЮ НАДО [ПОДНЯТЬ!!!](https://youtu.be/y75VErslEVQ?si=2RfhXgH58RR7_6_s)',
                     parse_mode='Markdown')


bot.infinity_polling()