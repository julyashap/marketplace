from src.product import Product
from src.mixin_repr import MixinRepr
from src.category_order import CategoryOrder
from src.zero_count_error import ZeroCountError


class Category(MixinRepr, CategoryOrder):
    """Класс категории продуктов на маркетплейсе"""

    count_categories = 0
    count_unique_products = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.count_categories += 1
        Category.count_unique_products = len(set(self.__goods))

        super().__init__()

    @property
    def goods(self):
        """Возвращает список объектов класса Product"""

        return self.__goods

    @property
    def get_goods(self):
        """Возвращает список объектов класса Product в формате: Продукт, 80 руб. Остаток: 15 шт."""

        printing_goods = ""

        for good in self.__goods:
            printing_goods += str(good) + "\n"

        return printing_goods

    @get_goods.setter
    def set_goods(self, product: Product):
        """Добавляет объект класса Product и его наследников в список товаров"""

        if not isinstance(product, Product):
            raise TypeError("Невозможно добавить этот тип!")

        if product.count_in_stock == 0:
            raise ZeroCountError

        try:
            self.__goods.append(product)
        except ZeroCountError as e:
            print(e)
        else:
            print("Товар успешно добавлен!")
        finally:
            print("Операция добавления товара завершена!")

    def __len__(self):
        """Возвращает длину списка объектов класса Product"""

        return sum(good.count_in_stock for good in self.__goods)

    def __str__(self):
        """Возвращает объект класса Category в формате: Название категории, количество продуктов: 200 шт."""

        return f"{self.name.title()}, количество продуктов: {len(self)} шт."

    def avg_cost_goods(self):
        """Возвращает средний ценник по всем товарам в списке __goods"""

        try:
            avg_cost = sum(good.get_cost for good in self.__goods) / len(self.__goods)
        except ZeroDivisionError:
            avg_cost = 0
        finally:
            return avg_cost
