from loader import bot
from data.database import MovieSearchHistory
from keyboard.inline import main_menu_keyboard


@bot.message_handler(text=['История поиска'])
def show_search_history(message):
    """
    Отображает историю поиска фильмов.
    """
    history_records = MovieSearchHistory.select().order_by(MovieSearchHistory.timestamp.desc()).limit(5)

    if history_records:
        response = "\n\n".join(
            [f"Название: {record.title}\nРейтинг: {record.rating}\nГод: {record.year}" for record in history_records]
        )
        bot.send_message(message.chat.id, f"История поиска:\n\n{response}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "История поиска пуста.", reply_markup=main_menu_keyboard())
