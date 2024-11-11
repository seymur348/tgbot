from api.kinopoisk import search_movie_by_rating
from loader import bot

def handle(message):
    try:
        args = message.text.split(" ", 2)  # Получаем аргументы команды
        rating = float(args[1])  # Рейтинг
        genre = args[2] if len(args) > 2 else None  # Жанр, если указан
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, "Пожалуйста, введите рейтинг (например, /movie_by_rating 8.5 [жанр]).")
        return

    movies = search_movie_by_rating(rating, genre)
    if movies:
        for movie in movies[:5]:  # Ограничиваем вывод до 5 фильмов
            title = movie["name"]
            description = movie.get("description", "Описание отсутствует")
            movie_rating = movie.get("rating", {}).get("kp", "Рейтинг отсутствует")
            year = movie.get("year", "Год отсутствует")
            genres = [genre.get("name", "Жанр отсутствует") for genre in movie.get("genres", [])]
            genre_str = ", ".join(genres)

            bot.send_message(
                message.chat.id,
                f"Название: {title}\nОписание: {description}\nРейтинг: {movie_rating}\nГод: {year}\nЖанр: {genre_str}"
            )
    else:
        bot.send_message(message.chat.id, "Фильмы с указанным рейтингом не найдены.")

