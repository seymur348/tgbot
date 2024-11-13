# handlers/history.py
from loader import bot
from data.database import SearchHistory
from telebot.types import Message
from keyboard.reply_keyboard import main_menu_keyboard

@bot.message_handler(commands=['history'])
def show_history(message: Message):
    user_id = message.from_user.id
    history_records = (
        SearchHistory
        .select()
        .where(SearchHistory.user_id == user_id)
        .order_by(SearchHistory.timestamp.desc())
        .limit(5)
    )

    if history_records:
        history_text = "\n\n".join([
            f"{record.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Тип поиска: {record.search_type}\n"
            f"Параметры: {record.search_params}"
            for record in history_records
        ])
        bot.send_message(message.chat.id, f"Последние запросы:\n\n{history_text}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "История запросов пуста.", reply_markup=main_menu_keyboard())
