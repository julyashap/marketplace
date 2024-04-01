import pytest
from src.category_order import CategoryOrder


def test_category_order():
    """Тест на проверку ошибки при создании экземпляра класса CategoryOrder"""

    with pytest.raises(TypeError):
        category_order = CategoryOrder(5)
