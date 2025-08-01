from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_language_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton("O'zbekcha")],
        [KeyboardButton("Русский")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

def get_contact_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        text = "Telefon raqamingizni yuboring:"
    else:
        text = "Отправьте ваш номер телефона:"

    keyboard = [[KeyboardButton(text, request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

def get_city_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        cities = ["Toshkent", "Samarqand", "Buxoro", "Andijon"]
    else:
        cities = ["Ташкент", "Самарканд", "Бухара", "Андижан"]

    keyboard = [[KeyboardButton(city)] for city in cities]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

def get_main_menu_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        keyboard = [
            [KeyboardButton("Buyurtma berish")],
            [KeyboardButton("Mening buyurtmalarim")],
            [KeyboardButton("Sozlamalar")],
        ]
    else:
        keyboard = [
            [KeyboardButton("Сделать заказ")],
            [KeyboardButton("Мои заказы")],
            [KeyboardButton("Настройки")],
        ]
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
