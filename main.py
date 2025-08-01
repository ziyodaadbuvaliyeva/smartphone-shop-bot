from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot.handlers import start, set_language, set_name, set_phone, set_city, cancel, main_menu
from bot.states import LANG, NAME, PHONE, CITY
from bot.config import TOKEN


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANG: [MessageHandler(Filters.text & ~Filters.command, set_language)],
            NAME: [MessageHandler(Filters.text & ~Filters.command, set_name)],
            PHONE: [MessageHandler(Filters.contact, set_phone)],
            CITY: [MessageHandler(Filters.text & ~Filters.command, set_city)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    dp.add_handler(conv_handler)

    # Menu handler (after registration)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, main_menu))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
