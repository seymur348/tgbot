from api.kinopoisk import search_movie
from data.database import save_search_history
from loader import bot


def handle(message):
    query = message.text.split(' ', 1)[-1]
    if not query or query == '/movie_search':
        bot.send_message(message.chat.id, "Пожалуйста, введите название фильма для поиска.")
        return

    # Запрос данных о фильме
    movies = search_movie(query)
    if isinstance(movies, list) and movies:
        movie = movies[0]  # Берем первый фильм из списка
        title = movie["name"]
        description = movie.get("description", "Описание отсутствует")
        rating = movie.get("rating", {}).get("kp", "Рейтинг отсутствует")
        year = movie.get("year", "Год отсутствует")

        # Извлекаем жанры, если они есть
        genres = [genre.get("name", "Жанр отсутствует") for genre in movie.get("genres", [])]
        genre = ", ".join(genres) if genres else "Жанр отсутствует"

        # Сохраняем историю поиска
        save_search_history(title, description, rating, year, genre)

        # Отправляем ответ пользователю
        bot.send_message(
            message.chat.id,
            f"Название: {title}\nОписание: {description}\nРейтинг: {rating}\nГод: {year}\nЖанр: {genre}"
        )
    else:
        bot.send_message(message.chat.id, "Фильм не найден.")
