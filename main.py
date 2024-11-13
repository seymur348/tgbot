from loader import bot, init_db
from telebot.types import Message
from keyboard.reply_keyboard import main_menu_keyboard
from handlers import movie_by_title, movie_by_rating, movie_by_budget, history, movie_details


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    """
    Обрабатывает команду /start, отправляя приветственное сообщение пользователю и
    отображая клавиатуру главного меню.

    :param message: Объект сообщения от пользователя.
    """
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=main_menu_keyboard())


if __name__ == '__main__':
    """
    Основной файл для запуска бота. Инициализирует базу данных и запускает бесконечный опрос бота.
    """
    init_db()  # Инициализация базы данных
    print("Бот запущен...")
    bot.infinity_polling()
