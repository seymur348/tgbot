from data.database import save_search_history
from loader import bot

def handle(message):
    history_records = get_search_history()

    if history_records:
        for record in history_records:
            bot.send_message(message.chat.id,
                             f"Название: {record.title}\nОписание: {record.description}\nРейтинг: {record.rating}\nГод: {record.year}\nЖанр: {record.genre}\n")
    else:
        bot.send_message(message.chat.id, "История поиска пуста.")
