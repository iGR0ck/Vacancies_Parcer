import json


class JsonSaver:
    def __init__(self, filename: str):
        self.filename = filename

    def save_to_json(self, vacancy: dict) -> json:

        with open(self.filename, 'a', encoding='UTF-8') as f:
            vacancy_data = {
                'Название вакансии': vacancy.title,
                'Место работы': vacancy.city,
                'Требования': vacancy.requirement,
                'Ссылка на вакансию': vacancy.url,
                'Зарплата': vacancy.payment
            }
            json.dump(vacancy_data, f, ensure_ascii=False)
            f.write('\n')


