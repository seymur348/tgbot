# database.py
import peewee
from datetime import datetime
from typing import Optional

db = peewee.SqliteDatabase('history.db')  # Файл базы данных


class SearchHistory(peewee.Model):
    user_id = peewee.IntegerField()
    search_type = peewee.CharField()  # Тип запроса (например, "Поиск по названию")
    search_params = peewee.CharField()  # Параметры поиска
    timestamp = peewee.DateTimeField(default=datetime.now)  # Время запроса

    class Meta:
        database = db


def init_db() -> None:
    """
    Инициализирует базу данных и создаёт таблицы.
    """
    if not db.is_closed():
        db.close()
    db.connect()
    db.create_tables([SearchHistory], safe=True)


def get_db_connection() -> peewee.SqliteDatabase:
    """
    Устанавливает соединение с базой данных.

    :return: Объект базы данных
    """
    if not db.is_closed():
        db.close()
    db.connect()
    return db
