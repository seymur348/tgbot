from loader import bot
from telebot.types import Message
from keyboard.reply_keyboard import main_menu_keyboard


@bot.message_handler(commands=['help'])
def help(message: Message) -> None:
    """
    Отправляет пользователю справочное сообщение о доступных командах.

    :param message: Объект сообщения от пользователя.
    """
    help_text = (
        "Список доступных команд:\n\n"
        "/start - Начать работу с ботом\n"
        "/help - Получить справочную информацию\n"
        "Поиск по названию - Найти фильмы по названию\n"
        "Поиск по рейтингу - Найти фильмы по минимальному рейтингу\n"
        "Поиск по бюджету - Найти фильмы по бюджету\n"
        "Детали фильма по ID - Получить подробности фильма по ID\n"
        "/history - Показать историю ваших запросов"
    )
    bot.send_message(message.chat.id, help_text, reply_markup=main_menu_keyboard())
