from loader import bot
from api.kinopoisk import get_movie_details


@bot.callback_query_handler(func=lambda call: call.data.startswith("details_"))
def send_movie_details(call):
    movie_id = call.data.split("_")[1]
    details = get_movie_details(movie_id)

    if details:
        title = details.get("name", "Название отсутствует")
        description = details.get("description", "Описание отсутствует")
        year = details.get("year", "Год отсутствует")
        rating = details.get("rating", {}).get("kp", "Рейтинг отсутствует")

        bot.send_message(
            call.message.chat.id,
            f"Подробная информация:\nНазвание: {title}\nОписание: {description}\nГод: {year}\nРейтинг: {rating}"
        )
    else:
        bot.send_message(call.message.chat.id, "Подробности о фильме не найдены.")
