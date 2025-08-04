from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


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
            [KeyboardButton("Gadget turini tanlang")],
            [KeyboardButton("Buyurtma berish"), KeyboardButton("Mening buyurtmalarim")],
            [KeyboardButton("Sozlamalar")],
        ]
    else:
        keyboard = [
            [KeyboardButton("Выберите тип гаджета")],
            [KeyboardButton("Сделать заказ"), KeyboardButton("Мои заказы")],
            [KeyboardButton("Настройки")],
        ]
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

def get_gadget_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("Telefon", callback_data="gadget:1")],
            [InlineKeyboardButton("Planshet", callback_data="gadget:2")],
            [InlineKeyboardButton("Smart Soat", callback_data="gadget:3")],
            [InlineKeyboardButton("Quloqchinlar", callback_data="gadget:4")],
        ]
    else:
        inline_keyboard = [
            [InlineKeyboardButton("Выберите тип 1", callback_data="gadget:1")],
            [InlineKeyboardButton("Выберите тип 2", callback_data="gadget:2")],
            [InlineKeyboardButton("Выберите тип 3", callback_data="gadget:3")],
            [InlineKeyboardButton("Выберите тип 4", callback_data="gadget:4")],
        ]
    
    return InlineKeyboardMarkup(inline_keyboard)
