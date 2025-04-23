import telebot

bot = telebot.TeleBot('ТОКЕН')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я простой бот.")

bot.polling()
