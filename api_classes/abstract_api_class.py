from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы с API сайтов c вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        pass