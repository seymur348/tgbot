from peewee import *
import datetime

# Настройка базы данных (например, SQLite)
db = SqliteDatabase('search_history.db')

class BaseModel(Model):
    class Meta:
        database = db

class SearchHistory(BaseModel):
    user_id = IntegerField()  # ID пользователя в Telegram
    query = CharField()  # Запрос пользователя
    description = TextField()  # Описание фильма
    rating = FloatField()  # Рейтинг фильма
    year = IntegerField()  # Год выпуска
    genre = CharField()  # Жанр фильма
    created_at = DateTimeField(default=datetime.datetime.now)  # Дата запроса

# Инициализация базы данных
def init_db():
    db.connect()
    db.create_tables([SearchHistory], safe=True)
