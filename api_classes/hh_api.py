import requests
from api_classes.abstract_api_class import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """
    Класс для работы с API HeadHunter для получения вакансий.
    """

    url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, keyword: str, per_page=10) -> list:

        params = {
            'text': keyword,
            'per_page': per_page,
            'only_with_salary': True
        }

        response = requests.get(self.url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data.get('items', [])
        else:
            print(f"Ошибка при запросе к API hh.ru: {response.status_code}")
            return []