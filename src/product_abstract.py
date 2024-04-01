from abc import ABC, abstractmethod


class ProductAbstract(ABC):
    """Абстрактный класс для продукта"""

    @abstractmethod
    def __init__(self, name: str, description: str, cost: float, count_in_stock: int):
        """Конструктор класса Product"""
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, products_dict: dict):
        """Возвращает объект класса Product из словаря"""
        pass

    @property
    @abstractmethod
    def get_cost(self):
        """Возвращает приватный атрибут __cost"""
        pass

    @get_cost.setter
    @abstractmethod
    def set_cost(self, new_cost: float):
        """Устанавливает значение приватного атрибута __cost с валидацией введенных данных"""
        pass

    @abstractmethod
    def __str__(self):
        """Возвращает объект класса Product в формате: Продукт, 80 руб. Остаток: 15 шт."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Возвращает сложение двух объектов класса Product и его наследников в виде сложения их стоимости,
                умноженной на количество на складе"""
        pass
