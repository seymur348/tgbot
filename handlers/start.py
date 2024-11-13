from loader import bot
from telebot.types import Message
from keyboard.reply_keyboard import main_menu_keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот для поиска фильмов. Выберите команду:",
        reply_markup=main_menu_keyboard()
    )
