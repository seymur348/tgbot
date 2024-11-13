from loader import bot
from data.database import SearchHistory
from telebot.types import Message
from keyboard.reply_keyboard import main_menu_keyboard


@bot.message_handler(commands=['history'])
def show_search_history(message: Message) -> None:
    """
    Показывает историю поиска фильмов для конкретного пользователя.

    :param message: Объект сообщения от пользователя.
    """
    user_id = message.from_user.id
    history_records = SearchHistory.select().where(SearchHistory.user_id == user_id).order_by(
        SearchHistory.timestamp.desc()).limit(10)

    if history_records:
        response = "\n\n".join([
            f"{record.timestamp.strftime('%Y-%m-%d %H:%M:%S')}: {record.search_type} - {record.search_params}"
            for record in history_records
        ])
        bot.send_message(message.chat.id, f"История поиска:\n\n{response}", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "История поиска пуста.", reply_markup=main_menu_keyboard())
