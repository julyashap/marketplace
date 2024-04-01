import pytest
from src.product_abstract import ProductAbstract


def test_product_abstract():
    """Тест на проверку ошибки при создании экземпляра класса ProductAbstract"""

    with pytest.raises(TypeError):
        product_abstract = ProductAbstract("Яблоко", "Полезный фрукт", 30.5, 53)
