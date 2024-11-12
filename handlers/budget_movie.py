from api.kinopoisk import search_movies_by_budget
from loader import bot
from keyboard.inline import main_menu_keyboard

@bot.message_handler(text=['Поиск по бюджету'])
def request_movie_budget(message):
    """
    Запрашивает у пользователя тип бюджета для поиска фильмов.
    """
    bot.send_message(message.chat.id, "Введите тип бюджета (низкий или высокий) и, при необходимости, жанр:")

@bot.message_handler(content_types=['text'])
def handle_movie_budget_search(message):
    """
    Обрабатывает тип бюджета и жанр, выполняет поиск и отправляет результаты.
    """
    args = message.text.split(" ", 1)
    budget_type = args[0].lower()
    genre = args[1] if len(args) > 1 else None

    if budget_type not in ["низкий", "высокий"]:
        bot.send_message(message.chat.id, "Пожалуйста, укажите корректный тип бюджета (низкий или высокий).")
        return

    budget_key = "low" if budget_type == "низкий" else "high"
    movies = search_movies_by_budget(budget_key, genre)

    if movies:
        response = "\n\n".join(
            [f"Название: {movie['name']}\nБюджет: {movie.get('budget', {}).get('value', 'Нет данных')}"
             for movie in movies[:5]]
        )
        bot.send_message(message.chat.id, f"Найденные фильмы:\n\n{response}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, f"Фильмы с {budget_type} бюджетом не найдены.", reply_markup=main_menu_keyboard())
