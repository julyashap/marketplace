class Category:
    """Класс категории продуктов на маркетплейсе"""

    count_categories = 0
    count_unique_products = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.count_categories += 1
        Category.count_unique_products = len(set(self.goods))

    @property
    def get_goods(self):
        return self.__goods

    @get_goods.setter
    def set_goods(self, product):
        self.__goods.append(product)
