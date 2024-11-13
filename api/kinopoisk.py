# api/kinopoisk.py
import os
import requests
from config_data.config import KINOPOISK_API_KEY
from dotenv import load_dotenv
from typing import Optional, List, Dict, Any

load_dotenv()
KINOPOISK_API_KEY = os.getenv('KINOPOISK_API_KEY')

BASE_URL = 'https://api.kinopoisk.dev/v1.3/movie'


def search_movie(title: str, genre: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Поиск фильма по названию с опциональным фильтром по жанру.

    :param title: Название фильма
    :param genre: Жанр фильма (опционально)
    :return: Список найденных фильмов с их данными
    """
    params = {
        "name": title,
        "token": KINOPOISK_API_KEY,
    }
    if genre:
        params["genres.name"] = genre

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if "docs" in data:
            return data["docs"]
        else:
            print(f"Некорректный ответ API: {data}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API Кинопоиска: {e}")
        return []


def search_movie_by_rating(min_rating: float, genre: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Поиск фильмов с минимальным рейтингом и опциональным фильтром по жанру.

    :param min_rating: Минимальный рейтинг фильма
    :param genre: Жанр фильма (опционально)
    :return: Список фильмов, соответствующих заданным критериям
    """
    params = {
        "rating.kp": f"{min_rating}-10",
        "token": KINOPOISK_API_KEY,
        "limit": 10
    }
    if genre:
        params["genres.name"] = genre

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("docs", [])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API Кинопоиска: {e}")
        return []


def search_movies_by_budget(budget_type: str, genre: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Поиск фильмов по бюджету (низкий или высокий) и опциональному жанру.

    :param budget_type: Тип бюджета ("low" для низкого, "high" для высокого)
    :param genre: Жанр фильма (опционально)
    :return: Список фильмов, соответствующих критериям бюджета и жанра
    """
    budget_limit = 10000000
    params = {
        "token": KINOPOISK_API_KEY,
        "limit": 10,
        "selectFields": "name rating.kp description",
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


def get_movie_details(movie_id: str) -> Optional[Dict[str, Any]]:
    """
    Получает полную информацию о фильме по его ID.

    :param movie_id: ID фильма
    :return: Полная информация о фильме
    """
    url = f"{BASE_URL}/{movie_id}"
    params = {"token": KINOPOISK_API_KEY}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API Кинопоиска: {e}")
        return None
