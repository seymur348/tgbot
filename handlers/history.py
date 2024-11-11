from data.database import MovieSearchHistory
from loader import bot


def handle(message):
    history_records = MovieSearchHistory.select().order_by(MovieSearchHistory.timestamp.desc()).limit(5)

    if history_records:
        for record in history_records:
            bot.send_message(message.chat.id,
                             f"Название: {record.title}\nОписание: {record.description}\nРейтинг: {record.rating}\nГод: {record.year}\nЖанр: {record.genre}\n")
    else:
        bot.send_message(message.chat.id, "История поиска пуста.")
