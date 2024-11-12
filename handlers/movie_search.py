from api.kinopoisk import search_movie
from loader import bot
from keyboard.inline import main_menu_keyboard

@bot.message_handler(text=['Поиск по названию'])
def request_movie_title(message):
    """
    Запрашивает у пользователя название фильма при выборе опции "Поиск по названию".
    """
    bot.send_message(message.chat.id, f"Введите название фильма: ")

@bot.message_handler(content_types=['text'])
def handle_movie_search(message):
    """
    Обрабатывает введенное название фильма, выполняет поиск и отправляет результаты.
    """
    title = message.text
    movies = search_movie(title)

    if movies:
        response = "\n\n".join(
            [f"Название: {movie['name']}\nРейтинг: {movie.get('rating', {}).get('kp', 'Нет данных')}"
             for movie in movies[:5]]
        )
        bot.send_message(message.chat.id, f"Найденные фильмы:\n\n{response}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Фильм не найден.", reply_markup=main_menu_keyboard())
