import telegram.ext

TOKEN = "5897888691:AAEuEgscYdvFmctozz79W9aSzyW2Y1kunto"


def start(update, context):
    update.message.reply_text("dit is wel degenlijk een 6.1 bot")
    update.message.reply_text("probeer ook: \n /help --> help \n /info --> info ")
   
    
def help(update, context):
    update.message.reply_text("6.1")

def info(update, context):
    update.message.reply_text("6.1 is gwn 6.1")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("info", info))

updater.start_polling()
updater.idle()

