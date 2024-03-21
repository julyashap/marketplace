from src.product import Product

class Category:
    """Класс категории продуктов на маркетплейсе"""

    count_categories = 0
    count_unique_products = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.count_categories += 1
        Category.count_unique_products = len(set(self.__goods))

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
        """Добавляет объект класса Product в список товаров"""

        self.__goods.append(product)

    def __len__(self):
        """Возвращает длину списка объектов класса Product"""

        count_products = 0

        for good in self.__goods:
            count_products += good.count_in_stock

        return count_products

    def __str__(self):
        """Возвращает объект класса Category в формате: Название категории, количество продуктов: 200 шт."""

        return f"{self.name.title()}, количество продуктов: {len(self)} шт."
