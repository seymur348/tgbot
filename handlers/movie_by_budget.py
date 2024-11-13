from loader import bot
from api.kinopoisk import search_movies_by_budget
from data.database import SearchHistory
from telebot.types import Message
from keyboard.reply_keyboard import budget_type_keyboard, main_menu_keyboard


@bot.message_handler(regexp="Поиск по бюджету")
def request_budget_type(message: Message) -> None:
    """
    Запрашивает у пользователя тип бюджета для поиска фильмов.
    """
    bot.send_message(message.chat.id, "Выберите тип бюджета:", reply_markup=budget_type_keyboard())
    bot.register_next_step_handler(message, handle_budget_type_selection)


def handle_budget_type_selection(message: Message) -> None:
    """
    Обрабатывает выбор пользователя по типу бюджета, выполняет поиск фильмов и отправляет результаты.

    :param message: Объект сообщения от пользователя, содержащий выбранный тип бюджета.
    """
    budget_type = "low" if message.text.lower() == "низкий" else "high" if message.text.lower() == "высокий" else None

    if budget_type:
        movies = search_movies_by_budget(budget_type)
        SearchHistory.create(
            user_id=message.from_user.id,
            search_type="Поиск по бюджету",
            search_params=f"Бюджет: {budget_type}"
        )

        if movies:
            response = "\n\n".join([
                f"Название: {movie['name']}\n"
                f"Рейтинг: {movie.get('rating', {}).get('kp', 'Нет данных')}\n"
                f"Описание: {movie.get('description', 'Описание недоступно')}"
                for movie in movies[:5]
            ])
            bot.send_message(message.chat.id, f"Найденные фильмы:\n\n{response}", reply_markup=main_menu_keyboard())
        else:
            bot.send_message(message.chat.id, "Фильмы с таким бюджетом не найдены.", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(message.chat.id, "Неверный выбор. Пожалуйста, выберите 'Низкий' или 'Высокий'.",
                         reply_markup=main_menu_keyboard())
