from loader import bot
from api.kinopoisk import search_movie_by_rating
from data.database import SearchHistory
from telebot.types import Message
from keyboard.reply_keyboard import main_menu_keyboard


@bot.message_handler(regexp="Поиск по рейтингу")
def request_min_rating(message: Message) -> None:
    """
    Запрашивает у пользователя минимальный рейтинг для поиска фильмов.
    """
    bot.send_message(message.chat.id, "Введите минимальный рейтинг фильма (например, 7.5):")
    bot.register_next_step_handler(message, handle_movie_rating_search)


def handle_movie_rating_search(message: Message) -> None:
    """
    Обрабатывает введенный минимальный рейтинг, выполняет поиск фильмов и отправляет результаты.

    :param message: Объект сообщения от пользователя, содержащий минимальный рейтинг.
    """
    try:
        min_rating = float(message.text.strip())
        movies = search_movie_by_rating(min_rating)

        SearchHistory.create(
            user_id=message.from_user.id,
            search_type="Поиск по рейтингу",
            search_params=f"Минимальный рейтинг: {min_rating}"
        )

        if movies:
            response = "\n\n".join([
                f"Название: {movie['name']}\n"
                f"Рейтинг: {movie.get('rating', {}).get('kp', 'Нет данных')}\n"
                f"Описание: {movie.get('description', 'Описание недоступно')}"
                for movie in movies[:5]
            ])
            bot.send_message(message.chat.id, f"Найденные фильмы:\n\n{response}", reply_markup=main_menu_keyboard())
        else:
            bot.send_message(message.chat.id, "Фильмы с таким рейтингом не найдены.", reply_markup=main_menu_keyboard())
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.", reply_markup=main_menu_keyboard())
