from src.product import Product
from src.mixin_repr import MixinRepr
from src.category_order import CategoryOrder
from src.zero_count_error import ZeroCountError


class Order(MixinRepr, CategoryOrder):
    """Класс заказа продукта в определенном количестве"""

    def __init__(self, product: Product, count_product: int):
        """Конструктор класса Order"""

        self.product = product
        self.count_product = count_product
        self.total_cost = count_product * product.get_cost

        super().__init__()

    def set_product(self, new_product: Product):
        """Устанавливает новое значение атрибута product"""

        if not isinstance(new_product, Product):
            raise TypeError("Невозможно добавить этот тип!")

        if new_product.count_in_stock == 0:
            raise ZeroCountError

        try:
            self.product = new_product
        except ZeroCountError as e:
            print(e)
        else:
            print("Товар успешно добавлен!")
        finally:
            print("Операция добавления товара завершена!")

    def __len__(self):
        """Возвращает длину объекта класса Order в виде количества продукта"""

        return self.count_product

    def __str__(self):
        """Возвращает строковое представление объекта класса Order"""

        return f"{self.product}\nКол-во: {self.count_product}, итоговая стоимость заказа: {self.total_cost}"
