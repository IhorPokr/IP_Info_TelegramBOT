from telegram.ext import *

import Constans
import Response


print("Bot started")


def start_command(update, context):
    update.message.reply_text("send me an IP and you will see all the info")


def info_message(update, context):
    ip_address = update.message.text
    response = Response.response_ip(ip_address)

    update.message.reply_text(response)


def main():
    updater = Updater(Constans.API_KEY)

    updater.dispatcher.add_handler(CommandHandler("start", start_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, info_message))
    updater.start_polling()


main()
