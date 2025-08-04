from telegram import Update
from telegram.ext import CallbackContext
from ..db import user_db
from ..keyboards.reply import get_gadget_keyboard


def send_gadgets(update: Update, context: CallbackContext) -> None:
    user_data = user_db.get_user(str(update.message.from_user.id))

    if 'language' not in user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, avval tilni tanlang.")
        return

    language = user_data['language']
    
    if language == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Gadget Turlari",
            reply_markup=get_gadget_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Главное меню:",
            reply_markup=get_gadget_keyboard("Русский")
        )
