from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def select_language_keyboard(language: str = 'uz') -> InlineKeyboardMarkup:
    """Create a keyboard for language selection."""
    keyboard = [
        [InlineKeyboardButton("O'zbekcha", callback_data='uz')],
        [InlineKeyboardButton("Русский", callback_data='ru')]
    ]
    return InlineKeyboardMarkup(keyboard)

def contact_keyboard(language: str) -> ReplyKeyboardMarkup:
    """Create a keyboard for contact sharing."""
    if language == 'uz':
        button_text = "Telefon raqamini yuborish"
    else:
        button_text = "Отправить номер телефона"

    keyboard = [
        [KeyboardButton(button_text, request_contact=True)]
    ]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
