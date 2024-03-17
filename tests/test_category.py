import pytest
from src.category import Category
from src.product import Product

@pytest.fixture
def category_exmpl():
    """Тестовый экземпляр класса Category"""

    return Category("Еда", "Для утоления голода", [Product("Яблоко", "Полезный фрукт", 30.5, 53),
                                                   Product("Пельмени", "Вкусный и сытный обед", 214.99, 152)])

def test_init(category_exmpl):
    """Тест конструктора класса Category"""

    assert category_exmpl.name == "Еда"
    assert category_exmpl.description == "Для утоления голода"
    assert category_exmpl.goods == [Product("Яблоко", "Полезный фрукт", 30.5, 53),
                                    Product("Пельмени", "Вкусный и сытный обед", 214.99, 152)]
    assert Category.count_categories == 1
    assert Category.count_unique_products == 2
