from telebot import TeleBot
from config_data.config import BOT_TOKEN
from data.database import init_db

# Создание экземпляра бота с использованием токена из конфигурации
bot: TeleBot = TeleBot(BOT_TOKEN)


def initialize_bot() -> None:
    """
    Инициализирует базу данных для хранения истории запросов пользователя.

    Функция вызывается при запуске бота для создания необходимых таблиц
    и выполнения любой предварительной настройки базы данных.
    """
    init_db()  # Инициализация базы данных


# Вызов инициализации базы данных при запуске модуля
initialize_bot()
