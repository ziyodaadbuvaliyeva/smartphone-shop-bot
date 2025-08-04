from telegram import Update
from telegram.ext import CallbackContext
from ..db import user_db, smartphone_db
from ..keyboards.reply import get_gadget_keyboard, get_telefon_keyboard, get_apple_telefon_keyboard


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


def send_telefonlar(update: Update, context: CallbackContext) -> None:
    user_data = user_db.get_user(str(update.effective_user.id))

    if 'language' not in user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, avval tilni tanlang.")
        return

    language = user_data['language']
    
    if language == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Telefonlar",
            reply_markup=get_telefon_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Telefonlar",
            reply_markup=get_telefon_keyboard("Русский")
        )


def send_apple_telefonlar(update: Update, context: CallbackContext) -> None:
    user_data = user_db.get_user(str(update.effective_user.id))

    if 'language' not in user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, avval tilni tanlang.")
        return

    language = user_data['language']
    
    if language == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Apple Telefonlar",
            reply_markup=get_apple_telefon_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Telefonlar",
            reply_markup=get_apple_telefon_keyboard("Русский")
        )

def send_apple_telefon(update: Update, context: CallbackContext) -> None:
    user_data = user_db.get_user(str(update.effective_user.id))

    if 'language' not in user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, avval tilni tanlang.")
        return

    language = user_data['language']
    
    if language == "O'zbekcha":
        for phone in smartphone_db.get_iphone_x():
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=phone['image_url'],
                caption=f"iPhone X\\price: {phone['price']}\ncolor: {phone['color']}",
            )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Telefonlar",
        )
