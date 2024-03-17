class Product:
    """Класс продукта на маркетплейсе"""

    count_products = 0

    def __init__(self, name: str, description: str, cost: float, count_in_stock: int):
        self.name = name
        self.description = description
        self.__cost = cost
        self.count_in_stock = count_in_stock

        Product.count_products += 1

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
    def set_cost(self, new_cost):
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
