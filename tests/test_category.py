import pytest
from src.category import Category

@pytest.fixture
def category_exmpl():
    """Тестовый экземпляр класса Category"""

    return Category("Еда", "Для утоления голода", ["Яблоко", "Шоколад", "Пельмени"])

def test_init(category_exmpl):
    """Тест конструктора класса Category"""

    assert category_exmpl.name == "Еда"
    assert category_exmpl.description == "Для утоления голода"
    assert category_exmpl.goods == ["Яблоко", "Шоколад", "Пельмени"]
    assert Category.count_categories == 1
    assert Category.count_unique_products == 0