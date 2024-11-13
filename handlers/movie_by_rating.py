# handlers/search_movie_by_rating_handler.py
from loader import bot
from api.kinopoisk import search_movie_by_rating
from keyboard.reply_keyboard import main_menu_keyboard
from telebot.types import Message


@bot.message_handler(regexp="Поиск по рейтингу")
def request_movie_rating(message):
    bot.send_message(message.chat.id, "Введите минимальный рейтинг фильма (например, 7) и, при необходимости, жанр:")
    bot.register_next_step_handler(message, handle_movie_rating_search)


def handle_movie_rating_search(message: Message):
    args = message.text.split(" ", 1)
    min_rating = args[0]
    genre = args[1] if len(args) > 1 else None

    # Вызов функции для поиска фильмов по рейтингу
    movies = search_movie_by_rating(min_rating, genre)

    if movies:
        response = "\n\n".join([
            f"Название: {movie.get('name', 'Нет данных')}\n"
            f"Рейтинг: {movie.get('rating', {}).get('kp', 'Нет данных')}\n"
            f"Описание: {movie.get('description', 'Описание недоступно')}"
            for movie in movies[:5]
        ])
        bot.send_message(message.chat.id, f"Найденные фильмы:\n\n{response}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Фильмы с указанным рейтингом не найдены.", reply_markup=main_menu_keyboard())
