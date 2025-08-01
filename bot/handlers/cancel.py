from telegram import Update
from telegram.ext import CallbackContext
from bot.handlers.menu import main_menu


def cancel(update: Update, context: CallbackContext) -> None:
    main_menu(update, context)
