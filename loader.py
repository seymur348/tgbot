import os
from dotenv import load_dotenv
from telebot import TeleBot
from data.database import init_db

# Загружаем переменные окружения из .env файла
load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Инициализация бота с токеном
bot = TeleBot(BOT_TOKEN)

# Инициализация базы данных
init_db()
