class Product:
    """Класс продукта на маркетплейсе"""

    count_products = 0

    def __init__(self, name: str, description: str, cost: float, count_in_stock: int):
        self.name = name
        self.description = description
        self.cost = cost
        self.count_in_stock = count_in_stock

        Product.count_products += 1
