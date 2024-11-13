from loader import bot
from api.kinopoisk import search_movie
from keyboard.reply_keyboard import main_menu_keyboard
from data.database import SearchHistory


@bot.message_handler(regexp="Поиск по названию")
def request_movie_title(message):
    """
    Запрашивает у пользователя название фильма для поиска.
    """
    bot.send_message(message.chat.id, "Введите название фильма и, при необходимости, жанр:")
    bot.register_next_step_handler(message, handle_movie_title_search)

def handle_movie_title_search(message):
    """
    Обрабатывает введенное название фильма и жанр, выполняет поиск и отправляет результаты.
    """
    args = message.text.split(" ", 1)
    title = args[0]
    genre = args[1] if len(args) > 1 else None

    movies = search_movie(title, genre)

    SearchHistory.create(
        user_id=message.from_user.id,
        search_type="Поиск по названию",
        search_params=f"{title} {genre if genre else ''}".strip()
    )
    if movies:
        # Формируем ответ с добавлением описания фильма
        response = "\n\n".join([
            f"Название: {movie['name']}\n"
            f"Рейтинг: {movie.get('rating', {}).get('kp', 'Нет данных')}\n"
            f"Описание: {movie.get('description', 'Описание недоступно')}"
            for movie in movies[:5]
        ])
        bot.send_message(message.chat.id, f"Найденные фильмы:\n\n{response}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Фильмы с таким названием не найдены.", reply_markup=main_menu_keyboard())


