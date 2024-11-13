from loader import bot
from telebot.types import Message
from keyboard.reply_keyboard import main_menu_keyboard


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    """
    Отправляет приветственное сообщение пользователю и отображает клавиатуру основного меню.

    :param message: Объект сообщения от пользователя.
    """
    bot.send_message(message.chat.id, "Добро пожаловать в бота поиска фильмов! Выберите действие:",
                     reply_markup=main_menu_keyboard())
