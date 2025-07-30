from config.token import TOKEN
from config.states import SELECT_LANGUAGE, CONTACT, PHONE, CITY

# import telegram modules
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackQueryHandler, ConversationHandler
from telegram.ext import Updater

# import handlers
from handlers.start_handler import start
from handlers.register import handle_language_selection, handle_contact


def main() -> None:
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_LANGUAGE: [CallbackQueryHandler(handle_language_selection, pattern='^(uz|ru)$')],
            CONTACT: [MessageHandler(Filters.contact, handle_contact)],
            PHONE: [MessageHandler(Filters.contact, start)],
            CITY: [MessageHandler(Filters.text & ~Filters.command, start)],
        },
        fallbacks=[],
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
