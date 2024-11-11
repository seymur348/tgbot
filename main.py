from loader import bot
from handlers import start, movie_search, movie_by_rating, low_budget_movie, high_budget_movie
from keyboard.inline import main_menu_keyboard, confirm_search_keyboard


# Команда /start для главного меню
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Бот поиска фильмов! Выберите действие:",
        reply_markup=main_menu_keyboard()
    )


# Обработчик для нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "search_by_title":
        bot.send_message(call.message.chat.id, "Введите название фильма:")
        bot.register_next_step_handler(call.message, movie_search.handle)

    elif call.data == "search_by_rating":
        bot.send_message(call.message.chat.id, "Введите минимальный рейтинг:")
        bot.register_next_step_handler(call.message, movie_by_rating.handle)

    elif call.data == "low_budget":
        bot.send_message(call.message.chat.id, "Введите жанр для фильмов с низким бюджетом (или оставьте пустым):")
        bot.register_next_step_handler(call.message, low_budget_movie.handle)

    elif call.data == "high_budget":
        bot.send_message(call.message.chat.id, "Введите жанр для фильмов с высоким бюджетом (или оставьте пустым):")
        bot.register_next_step_handler(call.message, high_budget_movie.handle)


# Подтверждение выполнения поиска
@bot.message_handler(commands=['confirm'])
def confirm_search(message):
    bot.send_message(message.chat.id, "Вы хотите выполнить поиск с указанными параметрами?",
                     reply_markup=confirm_search_keyboard())


@bot.callback_query_handler(func=lambda call: call.data == "confirm_search")
def execute_search(call):
    # Здесь выполняется поиск, выбранный пользователем
    bot.send_message(call.message.chat.id, "Поиск выполняется...")


@bot.callback_query_handler(func=lambda call: call.data == "cancel_search")
def cancel_search(call):
    bot.send_message(call.message.chat.id, "Поиск отменен. Вы можете вернуться в главное меню для нового выбора.")
    bot.send_message(call.message.chat.id, "Выберите действие:", reply_markup=main_menu_keyboard())


# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
