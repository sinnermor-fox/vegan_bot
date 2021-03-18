import logging

import requests
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import TG_TOKEN, PROXY
# from src.commands import food_per_day

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def main_keyboard():
    return ReplyKeyboardMarkup([['Menu']])


def menu_per_day(update, context):
    logging.info('Дай меню')
    # username = update.effective_chat.username
    response = requests.get('http://127.0.0.1:5000/menu/1')
    user_data = f"{response.json()['menu']}"
    update.message.reply_text(str(user_data), reply_markup=main_keyboard())

def greet_user(update, context):
    update.message.reply_text(f'Hi princess ')

def main():
    mybot = Updater(TG_TOKEN, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("menu", menu_per_day)),
    dp.add_handler(MessageHandler(Filters.regex('^(Menu)$'), menu_per_day))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
