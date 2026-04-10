import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# 👇 ТВОЙ ЮЗЕРНЕЙМ
CONTACT_USERNAME = "CNBZ0420"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет 👋\nНапиши /contact чтобы получить мой контакт"
    )

@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(
        message.chat.id,
        f"📞 Мой контакт:\nhttps://t.me/{CONTACT_USERNAME}"
    )

bot.infinity_polling()
