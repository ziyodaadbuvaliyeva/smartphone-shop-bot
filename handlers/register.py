from telegram import Update
from telegram.ext import callbackcontext

from keyboards.inline_kb import select_language_keyboard, contact_keyboard
from database.users import get_user, add_user, update_user

from config.states import SELECT_LANGUAGE, CONTACT, PHONE, CITY



def handle_language_selection(update: Update, context: callbackcontext.CallbackContext) -> int:
    """Handle the language selection."""
    query = update.callback_query
    query.answer()

    user_id = query.from_user.id
    language = query.data

    # Update user's language preference
    user = get_user(user_id)
    if user:
        user['language'] = language
        update_user(user_id, user)

    if language == 'uz':
        query.edit_message_text(
            f'Til tanlandi: Uzbekcha',
            reply_markup=None
        )
    else:
        query.edit_message_text(
            f'Язык выбран: Русский',
            reply_markup=None
        )

    # Ask for contact information
    if language == 'uz':
        query.message.reply_text(
            'Iltimos, telefon raqamingizni yuboring:',
            reply_markup=contact_keyboard(language)
        )
    else:
        query.message.reply_text(
            'Пожалуйста, отправьте свой номер телефона:',
            reply_markup=contact_keyboard(language)
        )

    return CONTACT


def handle_contact(update: Update, context: callbackcontext.CallbackContext) -> int:
    """Handle the contact information."""
    user_id = update.message.from_user.id
    contact = update.message.contact

    # Update user's contact information
    user = get_user(user_id)
    if user:
        user['phone'] = contact.phone_number
        update_user(user_id, user)

        print(f"User {user_id} phone updated to: {contact.phone_number}")

    if user['language'] == 'uz':
        update.message.reply_text('Telefon raqamingiz qabul qilindi. Shaharni kiriting:')
    else:
        update.message.reply_text('Ваш номер телефона принят. Пожалуйста, введите город:')

    return CITY


def handle_city(update: Update, context: callbackcontext.CallbackContext) -> int:
    """Handle the city information."""
    user_id = update.message.from_user.id
    city = update.message.text

    # Update user's city information
    user = get_user(user_id)
    if user:
        user['city'] = city
        update_user(user_id, user)

    if user['language'] == 'uz':
        update.message.reply_text('Shahar qabul qilindi. Ro\'yxatdan o\'tish tugallandi!')
    else:
        update.message.reply_text('Город принят. Регистрация завершена!')

    return -1  # End the conversation


