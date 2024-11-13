# handlers/movie_details_handler.py
from loader import bot
from api.kinopoisk import get_movie_details
from keyboard.reply_keyboard import main_menu_keyboard
from telebot.types import Message

@bot.message_handler(regexp="Детали фильма по ID")
def request_movie_id(message):
    bot.send_message(message.chat.id, "Введите ID фильма для получения детальной информации:")
    bot.register_next_step_handler(message, handle_movie_id_details)

def handle_movie_id_details(message: Message):
    movie_id = message.text.strip()

    movie = get_movie_details(movie_id)
    if movie:
        response = (
            f"Название: {movie.get('name', 'Нет данных')}\n"
            f"Год выпуска: {movie.get('year', 'Нет данных')}\n"
            f"Рейтинг: {movie.get('rating', {}).get('kp', 'Нет данных')}\n"
            f"Жанр: {', '.join([genre['name'] for genre in movie.get('genres', [])])}\n"
            f"Описание: {movie.get('description', 'Описание недоступно')}"
        )
        bot.send_message(message.chat.id, response, reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Не удалось найти детали для указанного ID.", reply_markup=main_menu_keyboard())
