import telegram.ext

TOKEN = "5897888691:AAEuEgscYdvFmctozz79W9aSzyW2Y1kunto"


def start(update, context):
    update.message.reply_text("de is wel degenlijk een 6.1 bot")


def help(update, context):
    update.message.reply_text("6.1")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))

updater.start_polling()
updater.idle()
