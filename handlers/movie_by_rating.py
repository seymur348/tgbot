from api.kinopoisk import search_movie_by_rating
from loader import bot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def create_rating_keyboard():
    keyboard = InlineKeyboardMarkup()
    search_again_button = InlineKeyboardButton("Найти другой фильм", callback_data="search_another_movie")
    keyboard.add(search_again_button)
    return keyboard

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

        # Отправляем сообщение с кнопками после отображения фильмов
        bot.send_message(
            message.chat.id,
            "Что вы хотите сделать дальше?",
            reply_markup=create_rating_keyboard()  # Добавляем клавиатуру с кнопками
        )
    else:
        bot.send_message(message.chat.id, "Фильмы с указанным рейтингом не найдены.")

