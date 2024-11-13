from loader import bot
from api.kinopoisk import get_movie_details
from telebot.types import Message
from keyboard.reply_keyboard import main_menu_keyboard


@bot.message_handler(regexp="Детали фильма по ID")
def request_movie_id(message: Message) -> None:
    """
    Запрашивает у пользователя ID фильма для получения детальной информации.
    """
    bot.send_message(message.chat.id, "Введите ID фильма для получения детальной информации:")
    bot.register_next_step_handler(message, handle_movie_id_details)


def handle_movie_id_details(message: Message) -> None:
    """
    Выполняет запрос к API для получения полной информации о фильме по ID.
    """
    movie_id = message.text.strip()
    movie = get_movie_details(movie_id)

    if movie:
        response = (
            f"Название: {movie.get('name', 'Нет данных')}\n"
            f"Год выпуска: {movie.get('year', 'Нет данных')}\n"
            f"Рейтинг: {movie.get('rating', {}).get('kp', 'Нет данных')}\n"
            f"Описание: {movie.get('description', 'Нет данных')}"
        )
        bot.send_message(message.chat.id, response, reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Фильм с данным ID не найден.", reply_markup=main_menu_keyboard())
