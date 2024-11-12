from api.kinopoisk import search_movie
from loader import bot
from keyboard.inline import movie_search_keyboard

def handle(message):
    query = message.text
    if not query:
        bot.send_message(message.chat.id, "Пожалуйста, введите название фильма для поиска.")
        return

    movies = search_movie(query)
    if isinstance(movies, list) and movies:
        bot.send_message(
            message.chat.id,
            "Выберите фильм для просмотра подробной информации:",
            reply_markup=movie_search_keyboard(movies[:5])  # Ограничиваем до 5 фильмов
        )
    else:
        bot.send_message(message.chat.id, "Фильм не найден.")
