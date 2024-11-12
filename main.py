from loader import bot
from keyboard.inline import main_menu_keyboard

@bot.message_handler(commands=['start'])
def start_command(message):
    """
    Обрабатывает команду /start и отображает главное меню.
    """
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Бот поиска фильмов! Выберите действие:",
        reply_markup=main_menu_keyboard()
    )
@bot.message_handler(commands=['movie_search'])
def search_movie_command(message):
    bot.send_message(
        message.chat.id,
        "Введите название фильма",
        reply_markup=main_menu_keyboard()

    )

if __name__ == "__main__":
    bot.infinity_polling()
