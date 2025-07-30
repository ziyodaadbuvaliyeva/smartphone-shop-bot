from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def select_language_keyboard():
    """Create a keyboard for language selection."""
    keyboard = [
        [InlineKeyboardButton("O'zbekcha", callback_data='uz')],
        [InlineKeyboardButton("Русский", callback_data='ru')]
    ]
    return InlineKeyboardMarkup(keyboard)
