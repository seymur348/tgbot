from loader import bot
from keyboard.reply_keyboard import main_menu_keyboard
from handlers import movie_by_title, movie_by_rating, movie_by_budget
from handlers import history, movie_details
from loader import init_db



@bot.message_handler(commands=['start'])
def start(message):
    """
    Стартовое сообщение и главное меню.
    """
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=main_menu_keyboard())

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
