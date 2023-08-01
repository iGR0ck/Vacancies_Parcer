import json


class JsonSaver:
    def __init__(self, filename):
        self.filename = filename

    def save_to_json(self, vacancy):

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

    def get_vacancies(self, criteri):
        vacancies = []
        with open(self.filename, "r") as f:
            for line in f:
                vacancy_data = json.loads(line)
                if self._vacancy_matches_criteria(vacancy_data, criteri):
                    vacancies.append(vacancy_data)
        return vacancies