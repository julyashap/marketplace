import pytest
from src.category_iteration import CategoryIteration
from src.category import Category
from src.product import Product

@pytest.fixture
def category_iteration_exmpl():
    """Тестовый экземпляр класса Category"""

    return CategoryIteration(Category("Техника", "Чтобы было удобнее жить",
                                      [Product("Iphone 15", "Очень крутой телефон", 130000.0, 13),
                                       Product("Телевизор", "Большой и в него можно смотреть", 60000.0, 31)]))


def test_init(category_iteration_exmpl):
    assert type(category_iteration_exmpl.category) == Category


def test_iter(category_iteration_exmpl):
    assert iter(category_iteration_exmpl) == category_iteration_exmpl
    assert category_iteration_exmpl.counter == -1


def test_next(category_iteration_exmpl):
    iterator = iter(category_iteration_exmpl)
    assert next(iterator) == category_iteration_exmpl.category.goods[0]
    assert next(iterator) == category_iteration_exmpl.category.goods[1]
    with pytest.raises(StopIteration):
        next(iterator)


def test_next_types(category_iteration_exmpl):
    iterator = iter(category_iteration_exmpl)
    assert type(next(iterator)) == Product
    assert type(next(iterator)) == Product
