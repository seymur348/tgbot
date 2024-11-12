from loader import bot
from data.database import MovieSearchHistory
from keyboard.inline import history_keyboard


def handle(message):
    history_records = MovieSearchHistory.select().order_by(MovieSearchHistory.timestamp.desc()).limit(5)

    if history_records:
        bot.send_message(
            message.chat.id,
            "Ваши последние найденные фильмы:",
            reply_markup=history_keyboard(history_records)
        )
    else:
        bot.send_message(message.chat.id, "История поиска пуста.")
