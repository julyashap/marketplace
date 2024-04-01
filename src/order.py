from src.product import Product
from src.mixin_repr import MixinRepr
from src.category_order import CategoryOrder


class Order(MixinRepr, CategoryOrder):
    def __init__(self, product: Product, count_product: int):
        self.product = product
        self.count_product = count_product
        self.total_cost = count_product * product.get_cost

        super().__init__()

    def __len__(self):
        return self.count_product

    def __str__(self):
        return f"{self.product}\nКол-во: {self.count_product}, итоговая стоимость заказа: {self.total_cost}"
