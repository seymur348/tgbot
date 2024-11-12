from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    """
    Главное меню с инлайн-кнопками для всех команд.
    """
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Поиск по названию", callback_data="search_by_title"),
        InlineKeyboardButton("Поиск по рейтингу", callback_data="search_by_rating")
    )
    markup.add(
        InlineKeyboardButton("Поиск по бюджету", callback_data="search_by_budget"),
        InlineKeyboardButton("История поиска", callback_data="search_history")
    )
    return markup

def movie_search_keyboard(movies):
    """
    Создает инлайн-клавиатуру для результатов поиска фильмов.
    """
    markup = InlineKeyboardMarkup()
    for movie in movies:
        markup.add(
            InlineKeyboardButton(
                movie["name"], callback_data=f"movie_{movie['id']}"
            )
        )
    return markup

def history_keyboard(movies):
    """
    Создает инлайн-клавиатуру для истории поиска, где каждая кнопка представляет найденный фильм.
    """
    markup = InlineKeyboardMarkup()
    for movie in movies:
        markup.add(
            InlineKeyboardButton(
                movie.title, callback_data=f"movie_{movie.id}"
            )
        )
    return markup
