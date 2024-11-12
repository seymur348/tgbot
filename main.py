from loader import bot
from handlers import movie_search, movie_by_rating, budget_movie, history
from keyboard.inline import main_menu_keyboard
from api.kinopoisk import get_movie_details  # Функция для получения информации о фильме по ID


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Бот поиска фильмов! Выберите действие:",
        reply_markup=main_menu_keyboard()
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "search_by_title":
        bot.send_message(call.message.chat.id, "Введите название фильма для поиска:")
        bot.register_next_step_handler(call.message, movie_search.handle)

    elif call.data == "search_by_rating":
        bot.send_message(call.message.chat.id, "Введите минимальный рейтинг (например, 8.5) и опционально жанр:")
        bot.register_next_step_handler(call.message, movie_by_rating.handle)

    elif call.data == "search_by_budget":
        bot.send_message(call.message.chat.id, "Введите тип бюджета (низкий или высокий) и опционально жанр:")
        bot.register_next_step_handler(call.message, budget_movie.handle)

    elif call.data == "search_history":
        history.handle(call.message)


@bot.callback_query_handler(func=lambda call: call.data.startswith("movie_"))
def show_movie_details(call):
    movie_id = call.data.split("_")[1]
    movie = get_movie_details(movie_id)
    if movie:
        title = movie["name"]
        description = movie.get("description", "Описание отсутствует")
        rating = movie.get("rating", {}).get("kp", "Рейтинг отсутствует")
        year = movie.get("year", "Год отсутствует")
        genres = [genre.get("name", "Жанр отсутствует") for genre in movie.get("genres", [])]
        genre_str = ", ".join(genres)

        bot.send_message(
            call.message.chat.id,
            f"Название: {title}\nОписание: {description}\nРейтинг: {rating}\nГод: {year}\nЖанр: {genre_str}"
        )
    else:
        bot.send_message(call.message.chat.id, "Информация о фильме не найдена.")
if __name__ == "__main__":
    bot.infinity_polling()