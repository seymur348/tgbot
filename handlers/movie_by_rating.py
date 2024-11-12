from api.kinopoisk import search_movie_by_rating
from loader import bot
from keyboard.inline import main_menu_keyboard

@bot.message_handler(text=['Поиск по рейтингу'])
def request_movie_rating(message):
    """
    Запрашивает у пользователя минимальный рейтинг для поиска фильма.
    """
    bot.send_message(message.chat.id, "Введите минимальный рейтинг (например, 8.5) и, при необходимости, жанр:")

@bot.message_handler(content_types=['text'])
def handle_movie_rating_search(message):
    """
    Обрабатывает введенный рейтинг и жанр, выполняет поиск и отправляет результаты.
    """
    try:
        args = message.text.split(" ", 1)
        min_rating = float(args[0])
        genre = args[1] if len(args) > 1 else None
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректный рейтинг.")
        return

    movies = search_movie_by_rating(min_rating, genre)
    if movies:
        response = "\n\n".join(
            [f"Название: {movie['name']}\nРейтинг: {movie.get('rating', {}).get('kp', 'Нет данных')}"
             for movie in movies[:5]]
        )
        bot.send_message(message.chat.id, f"Найденные фильмы:\n\n{response}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Фильмы с указанным рейтингом не найдены.", reply_markup=main_menu_keyboard())
