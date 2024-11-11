import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла

TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
KINOPOISK_API_KEY = os.getenv("KINOPOISK_API_KEY")
DB_NAME = 'movie_bot.db'
