from loader import bot
def handle(message):
    bot.send_message(message.chat.id, """
    /movie_search <название_фильма> - Поиск фильма по названию
    /movie_by_rating <рейтинг> - Поиск фильмов по рейтингу
    /low_budget_movie - Поиск фильмов с низким бюджетом
    /high_budget_movie - Поиск фильмов с высоким бюджетом
    /history - Просмотр истории запросов
    """)
