import requests
from api_classes.abstract_api_class import AbstractAPI
import os


class SuperJobAPI(AbstractAPI):
    """
    Класс для работы с API SuperJob для получения вакансий.
    """
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, keyword, count=10):
        api_token_sj = os.getenv('Superjob_API')
        headers = {
            "X-Api-App-Id": api_token_sj
        }
        params = {
            "keywords": [[1, keyword]],
            "count": count
        }

        response = requests.get(self.url, headers=headers, params=params)
        if response.status_code == 200:

            data = response.json()
            return data.get('objects', [])
        else:
            print(f"Ошибка при запросе к API superjob.ru: {response.status_code}")
            return []