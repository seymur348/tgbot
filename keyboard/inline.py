from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_keyboard():
    """
    Создает клавиатуру с кнопками для основных команд.
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Поиск по названию"))
    markup.add(KeyboardButton("Поиск по рейтингу"))
    markup.add(KeyboardButton("Поиск по бюджету"))
    markup.add(KeyboardButton("История поиска"))
    return markup
