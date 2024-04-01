from src.product import Product


class LawnGrass(Product):
    """Класс, определяющий газонную траву"""

    def __init__(self, name: str, description: str, cost: float, count_in_stock: int,
                 country: str, growing_period: float, color: str):
        """Конструктор класса LawnGrass"""

        self.country = country
        self.growing_period = growing_period
        self.color = color

        super().__init__(name, description, cost, count_in_stock)

    @classmethod
    def create_product(cls, products_dict: dict):
        """Возвращает объект класса LawnGrass из словаря"""

        return cls(products_dict['name'], products_dict['description'],
                   products_dict['price'], products_dict['quantity'],
                   products_dict['country'], products_dict['growing_period'],
                   products_dict['color'])

    def __repr__(self):
        """Возвращает строку в виде: НазваниеКласса(аргумент1, аргумент2, ...)"""

        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.get_cost}, " \
               f"{self.count_in_stock}, '{self.country}', {self.growing_period}, '{self.color}')"
