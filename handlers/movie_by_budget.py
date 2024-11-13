from loader import bot
from api.kinopoisk import search_movies_by_budget
from keyboard.reply_keyboard import budget_type_keyboard, main_menu_keyboard

@bot.message_handler(regexp="Поиск по бюджету")
def request_budget_type(message):
    """
    Запрашивает у пользователя тип бюджета для поиска фильма.
    """
    bot.send_message(message.chat.id, "Выберите тип бюджета:", reply_markup=budget_type_keyboard())
    bot.register_next_step_handler(message, handle_budget_type_search)

def handle_budget_type_search(message):
    """
    Обрабатывает выбранный тип бюджета и выполняет поиск.
    """
    budget_type = message.text.lower()
    if budget_type not in ["низкий", "высокий"]:
        bot.send_message(message.chat.id, "Пожалуйста, выберите правильный тип бюджета.", reply_markup=main_menu_keyboard())
        return

    genre = None  # Вы можете добавить дополнительный запрос для жанра, если хотите
    movies = search_movies_by_budget(budget_type, genre)
    if movies:
        response = "\n\n".join([
            f"Название: {movie['name']}\nБюджет: {movie.get('budget', {}).get('value', 'Нет данных')}"
            for movie in movies[:5]
        ])
        bot.send_message(message.chat.id, f"Найденные фильмы:\n\n{response}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Фильмы с указанным бюджетом не найдены.", reply_markup=main_menu_keyboard())
