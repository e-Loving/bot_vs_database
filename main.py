from database import *
import telebot
from config import token

bot = telebot.TeleBot(token)


@bot.message_handler()
def start_messaging(message):
    myString = ""
    if f"{message.text}".lower() in ["python", "kotlin", "php", "java", "javascript", "pascal"]:
        add(message.from_user.first_name, message.chat.id, message.text)
        for item in [item for item in fun()]:
            myString += item + "\n"
        bot.send_message(message.chat.id, f"{myString}")
    elif message.text == "delete":
        delete()


bot.polling(none_stop=True)
