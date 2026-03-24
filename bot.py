import telebot 
token =" "
bot = telebot.teleBot(token)
@bot.message_handler(commands=['start']) def start(massage):
  bot.reply_to(message,"hello in learning _both of my own ..")
  bot.infinity_polling()
