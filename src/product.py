from src.product_abstract import ProductAbstract
from src.mixin_repr import MixinRepr


class Product(MixinRepr, ProductAbstract):
    """Класс продукта на маркетплейсе"""

    count_products = 0

    def __init__(self, name: str, description: str, cost: float, count_in_stock: int):
        """Конструктор класса Product"""

        self.name = name
        self.description = description
        self.__cost = cost
        self.count_in_stock = count_in_stock

        Product.count_products += 1

        super().__init__()

    @classmethod
    def create_product(cls, products_dict: dict):
        """Возвращает объект класса Product из словаря"""

        return cls(products_dict['name'], products_dict['description'],
                   products_dict['price'], products_dict['quantity'])

    @property
    def get_cost(self):
        """Возвращает приватный атрибут __cost"""

        return self.__cost

    @get_cost.setter
    def set_cost(self, new_cost: float):
        """Устанавливает значение приватного атрибута __cost с валидацией введенных данных"""

        if new_cost <= 0:
            print("Некорректная цена!")

        elif new_cost < self.__cost:
            user_input = input("Вы действительно хотите понизить цену? "
                               "Введите 'y', если да, и 'n', если нет: ")

            if user_input == 'y':
                self.__cost = new_cost
                print("Цена изменена!")

        else:
            self.__cost = new_cost

    def __str__(self):
        """Возвращает объект класса Product в формате: Продукт, 80 руб. Остаток: 15 шт."""

        return f"{self.name.title()}, {self.__cost} руб. Остаток: {self.count_in_stock} шт."

    def __add__(self, other):
        """Возвращает сложение двух объектов класса Product и его наследников в виде сложения их стоимости,
        умноженной на количество на складе"""

        if type(other) == self.__class__:
            return self.__cost * self.count_in_stock + other.__cost * other.count_in_stock
        raise TypeError("Невозможно сложить эти типы!")
