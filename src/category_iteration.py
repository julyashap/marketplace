from src.category import Category
from src.product import Product

class CategoryIteration:
    """Класс для итерации по атрибуту __goods класса Category"""

    def __init__(self, category: Category):
        self.category = category

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        if self.counter + 1 < len(self.category.goods):
            self.counter += 1
            return self.category.goods[self.counter]
        else:
            raise StopIteration
