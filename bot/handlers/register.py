from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from bot.states import LANG, NAME, PHONE, CITY
from bot.keyboards.reply import get_contact_keyboard, get_city_keyboard
from bot.db import user_db
from bot.handlers.menu import main_menu


def set_language(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    language = update.message.text

    user_data = user_db.get_user(user_id)

    if language not in ["O'zbekcha", "Русский"]:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, to'g'ri tilni tanlang.")
        return LANG
    
    user_data['language'] = language
    user_db.set_user(user_id, user_data)

    if language == "O'zbekcha":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Til O'zbekcha sifatida o'rnatildi.")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ismingizni kiriting:")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Язык установлен на Русский.")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Введите ваше имя:")

    return NAME

def set_name(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    name = update.message.text

    user_data = user_db.get_user(user_id)
    user_data['name'] = name
    user_db.set_user(user_id, user_data)

    if user_data['language'] == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Telefon raqamingizni yuboring:",
            reply_markup=get_contact_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Введите ваш номер телефона:",
            reply_markup=get_contact_keyboard("Русский")
        )

    return PHONE

def set_phone(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    contact = update.message.contact

    user_data = user_db.get_user(user_id)
    user_data['phone'] = contact.phone_number
    user_db.set_user(user_id, user_data)

    if user_data['language'] == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Shahar nomini kiriting:",
            reply_markup=get_city_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Введите название города:",
            reply_markup=get_city_keyboard("Русский")
        )

    return CITY

def set_city(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    city = update.message.text

    user_data = user_db.get_user(user_id)
    user_data['city'] = city
    user_db.set_user(user_id, user_data)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!\n"
             f"Sizning ma'lumotlaringiz:\n"
             f"Til: {user_data['language']}\n"
             f"Ism: {user_data['name']}\n"
             f"Telefon: {user_data['phone']}\n"
             f"Shahar: {user_data['city']}"
    )

    main_menu(update, context)

    return ConversationHandler.END
