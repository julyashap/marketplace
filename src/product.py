class Product:
    """Класс продукта на маркетплейсе"""

    name: str
    description: str
    cost: float
    count_in_stock: int

    count_products = 0

    def __init__(self, name, description, cost, count_in_stock):
        self.name = name
        self.description = description
        self.cost = cost
        self.count_in_stock = count_in_stock

        Product.count_products += 1

