from api.kinopoisk import search_movie_by_rating
from loader import bot
from keyboard.inline import movie_search_keyboard

def handle(message):
    try:
        args = message.text.split(" ", 2)
        rating = float(args[1])
        genre = args[2] if len(args) > 2 else None
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, "Пожалуйста, введите рейтинг (например, /movie_by_rating 8.5 [жанр]).")
        return

    movies = search_movie_by_rating(rating, genre)
    if movies:
        bot.send_message(
            message.chat.id,
            "Выберите фильм для просмотра подробной информации:",
            reply_markup=movie_search_keyboard(movies[:5])  # Ограничиваем до 5 фильмов
        )
    else:
        bot.send_message(message.chat.id, "Фильмы с указанным рейтингом не найдены.")
