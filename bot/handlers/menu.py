from telegram import Update
from telegram.ext import CallbackContext
from bot.keyboards.reply import get_main_menu_keyboard
from bot.db import user_db


def main_menu(update: Update, context: CallbackContext) -> None:
    user_data = user_db.get_user(str(update.message.from_user.id))

    if 'language' not in user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, avval tilni tanlang.")
        return

    language = user_data['language']
    
    if language == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Asosiy menyu:",
            reply_markup=get_main_menu_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Главное меню:",
            reply_markup=get_main_menu_keyboard("Русский")
        )
