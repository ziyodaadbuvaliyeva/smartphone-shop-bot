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
            [InlineKeyboardButton("Telefon", callback_data="telefon")],
            [InlineKeyboardButton("Planshet", callback_data="plansher")],
            [InlineKeyboardButton("Smart Soat", callback_data="smart_soat")],
            [InlineKeyboardButton("Quloqchinlar", callback_data="quloqchinlar")],
        ]
    else:
        inline_keyboard = [
            [InlineKeyboardButton("Выберите тип 1", callback_data="gadget:1")],
            [InlineKeyboardButton("Выберите тип 2", callback_data="gadget:2")],
            [InlineKeyboardButton("Выберите тип 3", callback_data="gadget:3")],
            [InlineKeyboardButton("Выберите тип 4", callback_data="gadget:4")],
        ]
    
    return InlineKeyboardMarkup(inline_keyboard)

def get_telefon_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("Apple", callback_data="apple_telefon")],
            [InlineKeyboardButton("Samsung", callback_data="samsung_telefon")],
            [InlineKeyboardButton("Redmi Xiaomi", callback_data="redmi_telefon")],
        ]
    else:
        inline_keyboard = [
            [InlineKeyboardButton("Выберите тип 1", callback_data="gadget:1")],
            [InlineKeyboardButton("Выберите тип 2", callback_data="gadget:2")],
            [InlineKeyboardButton("Выберите тип 3", callback_data="gadget:3")],
            [InlineKeyboardButton("Выберите тип 4", callback_data="gadget:4")],
        ]
    
    return InlineKeyboardMarkup(inline_keyboard)

def get_apple_telefon_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("iPhone X", callback_data="apple_telefon_x")],
            [InlineKeyboardButton("iPhone 11", callback_data="apple_telefon_11")],
            [InlineKeyboardButton("iPhone 12", callback_data="apple_telefon_12")],
            [InlineKeyboardButton("iPhone 13", callback_data="apple_telefon_13")],
        ]
    else:
        inline_keyboard = [
            [InlineKeyboardButton("Выберите тип 1", callback_data="gadget:1")],
            [InlineKeyboardButton("Выберите тип 2", callback_data="gadget:2")],
            [InlineKeyboardButton("Выберите тип 3", callback_data="gadget:3")],
            [InlineKeyboardButton("Выберите тип 4", callback_data="gadget:4")],
        ]
    
    return InlineKeyboardMarkup(inline_keyboard)


def get_samsung_telefon_keyboard(language: str) -> InlineKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("Samsung Galaxy S21", callback_data="samsung_s21")],
            [InlineKeyboardButton("Samsung Galaxy Note 20", callback_data="samsung_note20")],
            [InlineKeyboardButton("Samsung Galaxy A52", callback_data="samsung_a52")],
        ]
    else:  
        inline_keyboard = [
            [InlineKeyboardButton("Самсунг Гэлакси S21", callback_data="samsung_s21")],
            [InlineKeyboardButton("Самсунг Гэлакси Нот 20", callback_data="samsung_note20")],
            [InlineKeyboardButton("Самсунг Гэлакси А52", callback_data="samsung_a52")],
        ]
    return InlineKeyboardMarkup(inline_keyboard)


def get_redmi_telefon_keyboard(language: str) -> InlineKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("Redmi Note 10", callback_data="redmi_note10")],
            [InlineKeyboardButton("Redmi Note 11", callback_data="redmi_note11")],
            [InlineKeyboardButton("Redmi 9C", callback_data="redmi_9c")],
        ]
    else:  
        inline_keyboard = [
            [InlineKeyboardButton("Редми Нот 10", callback_data="redmi_note10")],
            [InlineKeyboardButton("Редми Нот 11", callback_data="redmi_note11")],
            [InlineKeyboardButton("Редми 9C", callback_data="redmi_9c")],
        ]
    return InlineKeyboardMarkup(inline_keyboard)
