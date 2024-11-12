from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import bot

def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup()
    movie_search_button = InlineKeyboardButton("Поиск по названию", callback_data="search_by_title")
    movie_by_rating_button = InlineKeyboardButton("Поиск по рейтингу", callback_data="search_by_rating")
    low_budget_button = InlineKeyboardButton("Низкобюджетные фильмы", callback_data="low_budget")
    high_budget_button = InlineKeyboardButton("Высокобюджетные фильмы", callback_data="high_budget")
    keyboard.add(movie_search_button, movie_by_rating_button, low_budget_button, high_budget_button)
    return keyboard

def start_handler(message):
    """
    Обработчик команды /start. Отправляет приветственное сообщение
    с кнопками для выбора действия.
    """
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Бот поиска фильмов! Выберите действие:",
        reply_markup=main_menu_keyboard()  # Добавляем клавиатуру с кнопками
    )
