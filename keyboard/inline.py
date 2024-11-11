from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup()
    movie_search_button = InlineKeyboardButton("Поиск по названию", callback_data="search_by_title")
    movie_by_rating_button = InlineKeyboardButton("Поиск по рейтингу", callback_data="search_by_rating")
    low_budget_button = InlineKeyboardButton("Низкобюджетные фильмы", callback_data="low_budget_movies")
    high_budget_button = InlineKeyboardButton("Высокобюджетные фильмы", callback_data="high_budget_movies")
    history_button = InlineKeyboardButton("История запросов", callback_data="history")
    help_button = InlineKeyboardButton("Справка", callback_data="help")

    keyboard.add(movie_search_button, movie_by_rating_button)
    keyboard.add(low_budget_button, high_budget_button)
    keyboard.add(history_button, help_button)
    return keyboard

def search_action_keyboard():
    keyboard = InlineKeyboardMarkup()
    search_again_button = InlineKeyboardButton("Найти другой фильм", callback_data="search_another_movie")
    main_menu_button = InlineKeyboardButton("Вернуться в меню", callback_data="main_menu")

    keyboard.add(search_again_button)
    keyboard.add(main_menu_button)
    return keyboard
