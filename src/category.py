class Category:
    """Класс категории продуктов на маркетплейсе"""

    name: str
    description: str
    goods: list

    count_categories = 0
    count_unique_products = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.goods = goods

        Category.count_categories += 1
        Category.count_unique_products = len(set(self.goods))
