from loader import bot
from keyboard.inline import main_menu_keyboard

def handle(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Бот поиска фильмов! Выберите действие:",
        reply_markup=main_menu_keyboard()  # Добавляем клавиатуру с кнопками
    )
