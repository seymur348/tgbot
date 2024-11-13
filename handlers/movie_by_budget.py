# handlers/movie_by_budget.py
from loader import bot
from api.kinopoisk import search_movies_by_budget
from keyboard.reply_keyboard import main_menu_keyboard
from telebot.types import Message


@bot.message_handler(regexp="Поиск по бюджету")
def request_movie_budget(message: Message):
    """
    Запрашивает у пользователя тип бюджета (низкий или высокий) для поиска фильмов.
    """
    bot.send_message(message.chat.id, "Введите тип бюджета (низкий или высокий) и, при необходимости, жанр:")
    bot.register_next_step_handler(message, handle_movie_budget_search)


def handle_movie_budget_search(message: Message):
    args = message.text.split(" ", 1)
    budget_type = args[0].lower()
    genre = args[1] if len(args) > 1 else None

    # Выполняем поиск фильмов по бюджету
    movies = search_movies_by_budget(budget_type, genre)

    if movies:
        # Формируем ответ с проверкой на наличие ключей в каждом фильме
        response = "\n\n".join([
            f"Название: {movie.get('name', 'Нет данных')}\n"
            f"Рейтинг: {movie.get('rating', {}).get('kp', 'Нет данных')}\n"
            f"Описание: {movie.get('description', 'Описание недоступно')}"
            for movie in movies[:5]
        ])
        bot.send_message(message.chat.id, f"Найденные фильмы:\n\n{response}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Фильмы с указанным бюджетом не найдены.", reply_markup=main_menu_keyboard())
