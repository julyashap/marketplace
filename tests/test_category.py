import pytest
from src.category import Category
from src.product import Product
from src.zero_count_error import ZeroCountError


@pytest.fixture
def category_exmpl():
    """Тестовый экземпляр класса Category"""

    Product.count_products = 0

    return Category('Еда', 'Для утоления голода', [Product('Яблоко', 'Полезный фрукт', 30.5, 53),
                                                   Product('Пельмени', 'Вкусный и сытный обед', 214.99, 152)])


def test_init(category_exmpl):
    """Тест конструктора класса Category"""

    assert category_exmpl.name == "Еда"
    assert category_exmpl.description == "Для утоления голода"

    assert Category.count_categories == 1
    assert Category.count_unique_products == 2


def test_get_goods(category_exmpl):
    """Тест метода get_goods()"""

    assert category_exmpl.get_goods == "Яблоко, 30.5 руб. Остаток: 53 шт.\nПельмени, 214.99 руб. Остаток: 152 шт.\n"


def test_set_goods(category_exmpl):
    """Тест метода set_goods()"""

    category_exmpl.set_goods = Product("Мороженое", "Лакомство для всех", 54.99, 36)
    assert category_exmpl.get_goods == "Яблоко, 30.5 руб. Остаток: 53 шт.\nПельмени, 214.99 руб. Остаток: 152 шт.\n" \
                                       "Мороженое, 54.99 руб. Остаток: 36 шт.\n"

    with pytest.raises(TypeError, match="Невозможно добавить этот тип!"):
        category_exmpl.set_goods = 0

    with pytest.raises(ZeroCountError, match="Количество продукта не может быть нулевым!"):
        category_exmpl.set_goods = Product('Яблоко', 'Полезный фрукт', 30.5, 0)


def test_goods(category_exmpl):
    """Тест метода goods()"""

    assert category_exmpl.goods == category_exmpl._Category__goods


def test_len(category_exmpl):
    """Тест магического метода __len__()"""

    assert len(category_exmpl) == 205


def test_str(category_exmpl, capsys):
    """Тест магического метода __str__()"""

    assert str(category_exmpl) == "Еда, количество продуктов: 205 шт."
    assert type(str(category_exmpl)) == str

    print(category_exmpl)
    captured = capsys.readouterr()
    assert "Еда, количество продуктов: 205 шт." in captured.out


def test_avg_cost_goods(category_exmpl):
    assert category_exmpl.avg_cost_goods() == 122.745

    category = Category('Еда', 'Для утоления голода', [])
    assert category.avg_cost_goods() == 0
