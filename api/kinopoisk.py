import os

import requests
from config_data.config import KINOPOISK_API_KEY
from dotenv import load_dotenv
load_dotenv()
KINOPOISK_API_KEY = os.getenv('KINOPOISK_API_KEY')

BASE_URL = 'https://api.kinopoisk.dev/v1.3/movie'

def search_movie(title, genre=None):
    """
    Поиск фильма по названию с опциональным фильтром по жанру.
    """
    params = {
        "name": title,
        "token": KINOPOISK_API_KEY,
    }
    if genre:
        params["genres.name"] = genre  # Фильтр по жанру

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        # Проверяем, есть ли нужные данные
        if "docs" in data:
            return data["docs"]
        else:
            print(f"Некорректный ответ API: {data}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API Кинопоиска: {e}")
        return []

def search_movie_by_rating(min_rating, genre=None):
    """
    Поиск фильмов с минимальным рейтингом и опциональным фильтром по жанру.
    """
    params = {
        "rating.kp": f"{min_rating},10",  # Рейтинг от min_rating до 10
        "token": KINOPOISK_API_KEY,
        "limit": 10
    }
    if genre:
        params["genres.name"] = genre

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json().get("docs", [])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API Кинопоиска: {e}")
        return []

def search_movies_by_budget(budget_type, genre=None):
    """
    Поиск фильмов по бюджету (низкий или высокий) и опциональному жанру.
    """
    budget_limit = 10000000  # 10 миллионов
    params = {
        "token": KINOPOISK_API_KEY,
        "limit": 10
    }
    if budget_type == "low":
        params["budget.value"] = f"0,{budget_limit}"
    elif budget_type == "high":
        params["budget.value"] = f"{budget_limit},"

    if genre:
        params["genres.name"] = genre

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json().get("docs", [])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API Кинопоиска: {e}")
        return []

def get_movie_details(movie_id):
    """
    Получает полную информацию о фильме по его ID.
    """
    url = f"https://api.kinopoisk.dev/v1.3/movie/{movie_id}"
    params = {"token": KINOPOISK_API_KEY}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API Кинопоиска: {e}")
        return None