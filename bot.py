import constants as keys
from telegram import Update
from telegram.ext import *

print("Bot is waking up.")

async def deleteGroupStatusMessage(update: Update, context: CallbackContext):
    await context.bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)


def main():
    application = Application.builder().token(keys.API_KEY).build()

    application.add_handler(MessageHandler(filters.StatusUpdate.ALL, deleteGroupStatusMessage))

    application.run_polling(stop_signals=None)
    # application.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    # application.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)

if __name__ == "__main__":
    main()
