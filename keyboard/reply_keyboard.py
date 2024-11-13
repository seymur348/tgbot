from telebot import types

def main_menu_keyboard():
    """
    Основное меню бота с кнопками для выбора поиска.
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Поиск по названию", "Поиск по рейтингу", "Поиск по бюджету", "Детали фильма по ID")
    return keyboard

def budget_type_keyboard():
    """
    Клавиатура для выбора типа бюджета (низкий/высокий).
    """
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add("Низкий", "Высокий")
    keyboard.add("Вернуться в главное меню")
    return keyboard

def search_by_title_keyboard():
    """
    Клавиатура для поиска фильма по названию.
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Введите название фильма и, при необходимости, жанр.")
    keyboard.add("Вернуться в главное меню")
    return keyboard
