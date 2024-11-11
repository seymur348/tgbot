from telebot import TeleBot
from config_data.config import TELEGRAM_TOKEN
from data.database import init_db

bot = TeleBot(TELEGRAM_TOKEN)
init_db()


