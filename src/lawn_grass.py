from src.product import Product

class LawnGrass(Product):
    """Класс, определяющий газонную траву"""

    def __init__(self, name: str, description: str, cost: float, count_in_stock: int,
                 country: str, growing_period: float, color: str):
        """Конструктор класса LawnGrass"""

        super().__init__(name, description, cost, count_in_stock)

        self.country = country
        self.growing_period = growing_period
        self.color = color

    @classmethod
    def create_product(cls, products_dict: dict):
        """Возвращает объект класса LawnGrass из словаря"""

        return cls(products_dict['name'], products_dict['description'],
                   products_dict['price'], products_dict['quantity'],
                   products_dict['country'], products_dict['growing_period'],
                   products_dict['color'])
