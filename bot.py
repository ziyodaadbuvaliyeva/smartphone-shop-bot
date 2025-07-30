import config

# import telegram modules
from telegram.ext import CommandHandler
from telegram.ext import Updater

# import handlers
from handlers.start_handler import start


def main() -> None:
    updater = Updater(token=config.TOKEN)
    dispatcher = updater.dispatcher

    # add handlers
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
