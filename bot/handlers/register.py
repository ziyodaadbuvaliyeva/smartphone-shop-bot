from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from bot.states import LANG, NAME, PHONE, CITY
from bot.keyboards.reply import get_contact_keyboard, get_city_keyboard
from bot.db import user_db
from bot.handlers.menu import main_menu

def set_language(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    language = update.message.text

    if language not in ["O'zbekcha", "Русский"]:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, to'g'ri tilni tanlang.")
        return LANG  

    
    user_data = user_db.get_user(user_id) or {}
    user_data['language'] = language
    user_db.set_user(user_id, user_data)

    
    if language == "O'zbekcha":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Til O'zbekcha sifatida o'rnatildi.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Язык установлен на Русский.")

    
    main_menu(update, context)

    return NAME


def set_name(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    name = update.message.text

    user_data = user_db.get_user(user_id) or {}
    user_data['name'] = name
    user_db.set_user(user_id, user_data)

    if user_data.get('language') == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Telefon raqamingizni yuboring:",
            reply_markup=get_contact_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Введите ваш номер телефона:",
            reply_markup=get_contact_keyboard("Русский")
        )

    return PHONE


def set_phone(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    contact = update.message.contact

    user_data = user_db.get_user(user_id) or {}
    user_data['phone'] = contact.phone_number
    user_db.set_user(user_id, user_data)

    if user_data.get('language') == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Shahar nomini kiriting:",
            reply_markup=get_city_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Введите название города:",
            reply_markup=get_city_keyboard("Русский")
        )

    return CITY


def set_city(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    city = update.message.text

    user_data = user_db.get_user(user_id) or {}
    user_data['city'] = city
    user_db.set_user(user_id, user_data)

    lang = user_data.get('language', "O'zbekcha")

    if lang == "O'zbekcha":
        text = (
            f"Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!\n"
            f"Sizning ma'lumotlaringiz:\n"
            f"Til: {lang}\n"
            f"Ism: {user_data.get('name')}\n"
            f"Telefon: {user_data.get('phone')}\n"
            f"Shahar: {user_data.get('city')}"
        )
    else:
        text = (
            f"Регистрация успешно завершена!\n"
            f"Ваши данные:\n"
            f"Язык: {lang}\n"
            f"Имя: {user_data.get('name')}\n"
            f"Телефон: {user_data.get('phone')}\n"
            f"Город: {user_data.get('city')}"
        )

    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    main_menu(update, context)

    return ConversationHandler.END
