from api.kinopoisk import search_movies_by_budget
from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def handle_low_budget_movies(message):
    genre = message.text.split(" ", 1)[-1] if " " in message.text else None

    movies = search_movies_by_budget("low", genre)
    if movies:
        for movie in movies[:5]:  # Ограничиваем вывод до 5 фильмов
            title = movie["name"]
            description = movie.get("description", "Описание отсутствует")
            movie_budget = movie.get("budget", {}).get("value", "Бюджет отсутствует")
            year = movie.get("year", "Год отсутствует")
            genres = [genre.get("name", "Жанр отсутствует") for genre in movie.get("genres", [])]
            genre_str = ", ".join(genres)

            bot.send_message(
                message.chat.id,
                f"Название: {title}\nОписание: {description}\nБюджет: {movie_budget}\nГод: {year}\nЖанр: {genre_str}"
            )
    else:
        bot.send_message(message.chat.id, "Фильмы с низким бюджетом не найдены.")

def handle_high_budget_movies(message):
    genre = message.text.split(" ", 1)[-1] if " " in message.text else None

    movies = search_movies_by_budget("high", genre)
    if movies:
        for movie in movies[:5]:  # Ограничиваем вывод до 5 фильмов
            title = movie["name"]
            description = movie.get("description", "Описание отсутствует")
            movie_budget = movie.get("budget", {}).get("value", "Бюджет отсутствует")
            year = movie.get("year", "Год отсутствует")
            genres = [genre.get("name", "Жанр отсутствует") for genre in movie.get("genres", [])]
            genre_str = ", ".join(genres)

            bot.send_message(
                message.chat.id,
                f"Название: {title}\nОписание: {description}\nБюджет: {movie_budget}\nГод: {year}\nЖанр: {genre_str}"
            )
    else:
        bot.send_message(message.chat.id, "Фильмы с высоким бюджетом не найдены.")
