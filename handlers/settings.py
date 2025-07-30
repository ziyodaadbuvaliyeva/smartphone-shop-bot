from telegram import Update
from keyboards.inline_kb import select_language_keyboard


def send_language_selection_message(update: Update):
    """Send a message with language selection options."""
    update.message.reply_text(
        'Tilni tanlang | Выберите язык:', reply_markup=select_language_keyboard()
    )
