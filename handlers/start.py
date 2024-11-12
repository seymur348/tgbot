from keyboard.inline import main_menu_keyboard
from loader import bot

@bot.message_handler(text=['start'])
def start_handler(message):
    """
    Обработчик команды /start. Отправляет приветственное сообщение
    с кнопками для выбора действия.
    """
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Бот поиска фильмов! Выберите действие:",
        reply_markup=main_menu_keyboard()  # Добавляем клавиатуру с кнопками
    )
