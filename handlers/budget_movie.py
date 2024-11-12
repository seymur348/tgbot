from api.kinopoisk import search_movies_by_budget
from loader import bot
from keyboard.inline import movie_search_keyboard

def handle(message):
    args = message.text.split(" ", 2)
    if len(args) < 2 or args[1] not in ["низкий", "высокий"]:
        bot.send_message(message.chat.id, "Пожалуйста, укажите тип бюджета (низкий или высокий) и опционально жанр.")
        return

    budget_type = "low" if args[1] == "низкий" else "high"
    genre = args[2] if len(args) > 2 else None

    movies = search_movies_by_budget(budget_type, genre)
    if movies:
        bot.send_message(
            message.chat.id,
            "Выберите фильм для просмотра подробной информации:",
            reply_markup=movie_search_keyboard(movies[:5])  # Ограничиваем до 5 фильмов
        )
    else:
        bot.send_message(message.chat.id, f"Фильмы с {args[1]} бюджетом не найдены.")
