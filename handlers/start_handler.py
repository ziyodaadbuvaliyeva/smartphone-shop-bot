from telegram import Update
from telegram.ext import callbackcontext
from .settings import send_language_selection_message


def start(update: Update, context: callbackcontext.CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Assalomu alaykum! Bizning botimizda istalgan gadgetni qulay narxlarda online xarid qilishingiz mumkin.\n\n'
        'Вы можете купить любое устройство в нашем боте по удобной цене онлайн.\n\n'
        'Talab va takliflar uchun | Для запросов и предложений: @smartphoneshop_support'
    )
    send_language_selection_message(update)
