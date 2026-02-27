from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# توکن رباتتو اینجا بزار
TOKEN = "8785387571:AAGvEFzePljSPe8mjLgewtqmJhGAk1h23i0"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! رباتت فعال شد ✅")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
