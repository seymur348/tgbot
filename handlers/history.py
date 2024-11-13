# handlers/history_handler.py
from loader import bot
from data.database import SearchHistory  # Импортируем модель для работы с базой данных
from telebot.types import Message
from keyboard.reply_keyboard import main_menu_keyboard


@bot.message_handler(commands=['history'])
def show_search_history(message: Message):
    # Получаем историю запросов пользователя из базы данных
    user_history = SearchHistory.select().where(SearchHistory.user_id == message.from_user.id)

    if user_history:
        response = "Ваша история запросов:\n\n"
        for record in user_history:
            response += (
                f"Запрос: {record.query}\n"
                f"Описание: {record.description}\n"
                f"Рейтинг: {record.rating}\n"
                f"Год: {record.year}\n"
                f"Жанр: {record.genre}\n"
                f"Дата запроса: {record.created_at}\n\n"
            )
        bot.send_message(message.chat.id, response, reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Ваша история запросов пуста.", reply_markup=main_menu_keyboard())
