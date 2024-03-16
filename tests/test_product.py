import pytest
from src.product import Product

@pytest.fixture
def product_exmpl():
    """Тестовый экземпляр класса Product"""

    return Product("Яблоко", "Полезный фрукт", 30.5, 53)

def test_init(product_exmpl):
    """Тест конструктора класса Product"""

    assert product_exmpl.name == "Яблоко"
    assert product_exmpl.description == "Полезный фрукт"
    assert product_exmpl.cost == 30.5
    assert product_exmpl.count_in_stock == 53
    assert Product.count_products == 1