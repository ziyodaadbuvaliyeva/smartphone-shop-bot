from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def contact_keyboard(language: str) -> InlineKeyboardMarkup:
    """Create a keyboard for contact sharing."""
    if language == 'uz':
        button_text = "Telefon raqamini yuborish"
    else:
        button_text = "Отправить номер телефона"

    keyboard = [
        [InlineKeyboardButton(button_text, request_contact=True)]
    ]
    return InlineKeyboardMarkup(keyboard)
