from telegram import Update
from telegram.ext import callbackcontext

from database.users import load_users, save_users, get_user, add_user, update_user

from config.states import SELECT_LANGUAGE

from keyboards.inline_kb import select_language_keyboard


def start(update: Update, context: callbackcontext.CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user_id = update.message.from_user.id

    user = get_user(user_id)
    if not user:
        update.message.reply_text(
            'Assalomu alaykum! Bizning botimizda istalgan gadgetni qulay narxlarda online xarid qilishingiz mumkin.\n\n'
            'Вы можете купить любое устройство в нашем боте по удобной цене онлайн.\n\n'
            'Talab va takliflar uchun | Для запросов и предложений: @smartphoneshop_support'
        )

        update.message.reply_text(
            'Tilni tanlang | Выберите язык:', reply_markup=select_language_keyboard()
        )

        add_user(user_id, {
            'language': 'uz',
            'phone': None,
            'city': None,
            'cart': []
        })
    else:
        update.message.reply_text(
            'Assalomu alaykum! Siz allaqachon botimizda ro\'yxatdan o\'tgansiz.\n\n'
            'Вы уже зарегистрированы в нашем боте.\n\n'
            'Talab va takliflar uchun | Для запросов и предложений: @smartphoneshop_support'
        )

    return SELECT_LANGUAGE
