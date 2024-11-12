# handlers/callback_handler.py
from telebot import types
from api.kinopoisk import get_movie_details
from loader import bot
# Предполагается, что такая функция есть в API


def send_movie_details(call):
    # Получаем ID фильма из callback_data
    movie_id = call.data.split('_')[1]  # Допустим, callback_data выглядит как 'movie_123'

    # Получаем информацию о фильме
    movie_info = get_movie_details(movie_id)

    # Проверяем, что movie_info не None
    if movie_info:
        # Формируем сообщение с информацией о фильме
        message = f"Название: {movie_info['title']}\n"
        message += f"Рейтинг: {movie_info['rating']}\n"
        message += f"Описание: {movie_info['description']}\n"

        # Отправляем ответ в чат
        bot.send_message(call.message.chat.id, message)

        # Можно добавить кнопки для взаимодействия с пользователем
        keyboard = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton("Назад", callback_data="back")
        keyboard.add(back_button)

        bot.send_message(call.message.chat.id, "Вот информация о фильме:", reply_markup=keyboard)
    else:
        # Если movie_info None, информируем пользователя
        bot.send_message(call.message.chat.id, "Извините, информация о фильме не найдена.")
