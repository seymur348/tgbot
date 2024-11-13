# database.py
import peewee
from datetime import datetime

db = peewee.SqliteDatabase('history.db')  # Файл базы данных

class SearchHistory(peewee.Model):
    user_id = peewee.IntegerField()
    search_type = peewee.CharField()       # Тип запроса (например, "Поиск по названию")
    search_params = peewee.CharField()     # Параметры поиска
    timestamp = peewee.DateTimeField(default=datetime.now)  # Время запроса

    class Meta:
        database = db

# Инициализация базы данных и таблицы
def init_db():
    if not db.is_closed():
        db.close()  # Закрываем, если база данных уже открыта
    db.connect()
    db.create_tables([SearchHistory], safe=True)
def get_db_connection():
    if not db.is_closed():
        db.close()  # Закрываем, если база данных уже открыта
    db.connect()
    return db
# Вызываем инициализацию при запуске
init_db()
