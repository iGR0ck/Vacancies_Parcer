from api_classes.hh_api import HeadHunterAPI
from api_classes.superjob_api import SuperJobAPI
from utils.vacancies import Vacancy
from files.json_vacancy import JsonSaver
import json


def user_interaction():
    """
   Функция для взаимодействия с пользователем.
   Пользователь вводит поисковый запрос, количество вакансий для вывода в топ N и ключевые слова для фильтрации.
   Затем программа получает вакансии с платформ hh.ru и superjob.ru, фильтрует и сортирует результаты и выводит топ N вакансий согласно заданным критериям.
   """
    site_list_for_search = ['HeadHunter', 'SuperJob']
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    user_search = input("Введите поисковый запрос: ")
    top_search = int(input("Введите количество вакансий для вывода в топ N: "))

    hh_vacancies = hh_api.get_vacancies(user_search.lower(), top_search)
    superjob_vacancies = superjob_api.get_vacancies(user_search.lower(), top_search)

    json_saver_hh = JsonSaver('user_hh.json')
    for vacancy in hh_vacancies:
        vacancy_title = vacancy['name']  # название вакансии
        vacancy_requirement = vacancy['snippet']['requirement']  # описание вакансии
        vacancy_url = vacancy['url']  # url
        vacancy_city = vacancy['area']['name']  # название города для поиска
        if vacancy['salary']['from'] == 0 or vacancy['salary']['from'] is None:

            vacancy_pay = 'Зарплата не указана'

        else:
            vacancy_pay = vacancy['salary']['from']
        vacancy = Vacancy(vacancy_title, vacancy_city, vacancy_requirement, vacancy_url, vacancy_pay)
        json_saver_hh.save_to_json(vacancy)

    json_saver_sj = JsonSaver('user_sj.json')
    for vacancy in superjob_vacancies:
        vacancy_title = vacancy['profession']  # название вакансии
        vacancy_requirement = vacancy['candidat']  # описание вакансии
        vacancy_url = vacancy['link']  # url
        vacancy_city = vacancy['address']  # название города для поиска
        if vacancy['payment_from'] == 0 or vacancy['payment_from'] is None:

            vacancy_pay = 'Зарплата не указана'

        else:
            vacancy_pay = vacancy['payment_from']
        vacancy = Vacancy(vacancy_title, vacancy_city, vacancy_requirement, vacancy_url, vacancy_pay)
        json_saver_sj.save_to_json(vacancy)

    print('Данные сохранены в соответствующие файлы')

    user_answer = input('Вывести список вакансий? (да\нет) :')
    if user_answer.lower() == 'да':
        user_count = int(input(f'С какой площадки вывести данные?\n'
                               f'1. {site_list_for_search[0]}\n'
                               f'2. {site_list_for_search[1]}\n'))
        if user_count == 1:
            vacancies = []
            with open('user_hh.json', encoding='UTF-8') as f:
                for line in f:
                    vacancy_data = json.loads(line)
                    vacancies.append(vacancy_data)
            for v in vacancies:
                print(v)
        elif user_count == 2:
            vacancies = []
            with open('user_sj.json', encoding='UTF-8') as f:
                for line in f:
                    vacancy_data = json.loads(line)
                    vacancies.append(vacancy_data)
            for v in vacancies:
                print(v)
        else:
            print('Неверный ввод')
    elif user_answer.lower() == 'нет':
        print('Вы можете посмотреть вакансии в файле.')
    else:
        print('Неверный ввод')

    user_answer = input('Очистить файлы с вакансиями? (да\нет) : ')
    if user_answer.lower() == 'да':
        with open("user_hh.json", "w") as f:
            pass
        with open("user_sj.json", "w") as f:
            pass
    else:
        print('Программа завершена')