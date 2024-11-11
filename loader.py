import os
from dotenv import load_dotenv
from telebot import TeleBot
from data.database import init_db

# Загрузка токенов из .env файла
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = TeleBot(BOT_TOKEN)  # Инициализация бота с токеном

# Инициализация базы данных
init_db()
