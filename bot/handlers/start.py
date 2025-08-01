from telegram import Update
from telegram.ext import CallbackContext
from bot.states import LANG, NAME, PHONE, CITY
from bot.keyboards.reply import get_language_keyboard
from bot.db import user_db


def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user = user_db.get_user(user_id)

    if not user:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Salom, Botga xush kelibsiz!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Xush kelibsiz!")

    update.message.reply_text(
        "Iltimos, tilni tanlang:",
        reply_markup=get_language_keyboard()
    )

    return LANG

