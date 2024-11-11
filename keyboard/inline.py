from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    """
    Главное меню с кнопками для выбора типа поиска.
    """
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Поиск по названию", callback_data="search_by_title"),
        InlineKeyboardButton("Поиск по рейтингу", callback_data="search_by_rating")
    )
    markup.add(
        InlineKeyboardButton("Поиск по бюджету (низкий)", callback_data="low_budget"),
        InlineKeyboardButton("Поиск по бюджету (высокий)", callback_data="high_budget")
    )
    return markup

def confirm_search_keyboard():
    """
    Кнопки для подтверждения или отмены поиска.
    """
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Подтвердить", callback_data="confirm_search"),
        InlineKeyboardButton("Отмена", callback_data="cancel_search")
    )
    return markup
