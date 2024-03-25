from src.product import Product

class Smartphone(Product):
    """Класс, определяющий телефон"""

    def __init__(self, name: str, description: str, cost: float, count_in_stock: int,
                 capacity: int, model: str, memory: int, color: str):
        """Конструктор класса Smartphone"""

        super().__init__(name, description, cost, count_in_stock)

        self.capacity = capacity
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def create_product(cls, products_dict: dict):
        """Возвращает объект класса Smartphone из словаря"""

        return cls(products_dict['name'], products_dict['description'],
                   products_dict['price'], products_dict['quantity'],
                   products_dict['capacity'], products_dict['model'],
                   products_dict['memory'], products_dict['color'])
