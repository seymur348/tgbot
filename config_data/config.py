import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()  # Загружаем переменные окружения для безопасного использования API-ключей и токенов

# Токен для бота, получаем из переменных окружения
BOT_TOKEN: str = os.getenv("BOT_TOKEN")  # Тип данных: строка

# Ключ API для работы с Кинопоиском, получаем из переменных окружения
KINOPOISK_API_KEY: str = os.getenv("KINOPOISK_API_KEY")  # Тип данных: строка

# Имя базы данных для бота, используется для подключения к SQLite
DB_NAME: str = 'movie_bot.db'  # Тип данных: строка
