from peewee import *
from config_data.config import DB_NAME

db = SqliteDatabase(DB_NAME)

class MovieSearchHistory(Model):
    title = CharField()
    description = TextField()
    rating = CharField()
    year = IntegerField()
    genre = CharField()
    timestamp = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        database = db

def init_db():
    db.connect()
    db.create_tables([MovieSearchHistory], safe=True)

def save_search_history(title, description, rating, year, genre):
    MovieSearchHistory.create(title=title, description=description, rating=rating, year=year, genre=genre)
