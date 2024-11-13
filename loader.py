from telebot import TeleBot
from config_data.config import BOT_TOKEN
from data.database import init_db

bot = TeleBot(BOT_TOKEN)
init_db()  # Инициализация базы данных

