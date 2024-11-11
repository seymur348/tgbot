from loader import bot
from handlers import start_handler, movie_search_handler, rating_search_handler, handle_low_budget_movies, handle_high_budget_movies, history_handler

@bot.message_handler(commands=['start'])
def start_command(message):
    start_handler(message)

@bot.message_handler(commands=['movie_search'])
def movie_search_command(message):
    movie_search_handler(message)

@bot.message_handler(commands=['low_budget_movie'])
def low_budget_command(message):
    handle_low_budget_movies(message)

@bot.message_handler(commands=['high_budget_movie'])
def high_budget_command(message):
    handle_high_budget_movies(message)

@bot.callback_query_handler(func=lambda call: call.data == "search_by_title")
def callback_search_by_title(call):
    bot.send_message(call.message.chat.id, "Пожалуйста, введите название фильма для поиска.")

@bot.callback_query_handler(func=lambda call: call.data == "search_by_rating")
def callback_search_by_rating(call):
    bot.send_message(call.message.chat.id, "Пожалуйста, введите рейтинг для поиска фильмов.")

@bot.callback_query_handler(func=lambda call: call.data == "low_budget_movies")
def callback_low_budget(call):
    return low_budget_command(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "high_budget_movies")
def callback_high_budget(call):
    return high_budget_command(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "history")
def callback_history(call):
    history_handler(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "search_another_movie")
def handle_search_another_movie(call):
    bot.send_message(call.message.chat.id, "Пожалуйста, введите новый рейтинг или название фильма для поиска.")

@bot.callback_query_handler(func=lambda call: call.data == "main_menu")
def handle_main_menu(call):
    start_command(call.message)

if __name__ == "__main__":
    bot.polling(none_stop=True)
