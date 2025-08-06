from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,
    CallbackQueryHandler,
)
from bot.handlers import (
    start, set_language, set_name, set_phone, set_city, cancel, main_menu,
    send_gadgets, send_telefonlar, send_apple_telefonlar, send_apple_telefon,
    send_samsung_telefonlar, send_redmi_telefonlar  
)
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
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True  
    )

    dp.add_handler(conv_handler)

    
    dp.add_handler(MessageHandler(Filters.text(["Gadget turini tanlang", "Выберите тип гаджета"]), send_gadgets))

    
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, main_menu))

    
    dp.add_handler(CallbackQueryHandler(send_telefonlar, pattern='telefon'))
    dp.add_handler(CallbackQueryHandler(send_apple_telefon, pattern='apple_telefon_x'))
    dp.add_handler(CallbackQueryHandler(send_apple_telefonlar, pattern='apple_telefon'))
    dp.add_handler(CallbackQueryHandler(send_samsung_telefonlar, pattern='samsung_telefon'))
    dp.add_handler(CallbackQueryHandler(send_redmi_telefonlar, pattern='redmi_telefon'))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
