import pytest
from src.order import Order
from src.product import Product
from src.zero_count_error import ZeroCountError


@pytest.fixture
def order_exmpl():
    Product.count_products = 0

    return Order(Product('Груша', 'Полезный фрукт', 60.0, 24), 15)


@pytest.fixture
def product_exmpl():
    """Тестовый экземпляр класса Product"""

    Product.count_products = 0

    return Product('Яблоко', 'Полезный фрукт', 30.5, 53)


def test_init(order_exmpl):
    assert type(order_exmpl.product) == Product
    assert order_exmpl.count_product == 15
    assert order_exmpl.total_cost == 900.0


def test_len(order_exmpl):
    assert len(order_exmpl) == 15


def test_str(order_exmpl, capsys):
    assert str(order_exmpl) == """Груша, 60.0 руб. Остаток: 24 шт.
Кол-во: 15, итоговая стоимость заказа: 900.0"""
    assert type(str(order_exmpl)) == str

    print(order_exmpl)
    captured = capsys.readouterr()
    assert """Груша, 60.0 руб. Остаток: 24 шт.
Кол-во: 15, итоговая стоимость заказа: 900.0""" in captured.out


def test_set_product(order_exmpl, product_exmpl):
    with pytest.raises(TypeError, match="Невозможно добавить этот тип!"):
        order_exmpl.set_product(0)

    with pytest.raises(ZeroCountError, match="Количество продукта не может быть нулевым!"):
        order_exmpl.set_product(Product('Яблоко', 'Полезный фрукт', 30.5, 0))

    order_exmpl.set_product(product_exmpl)
    assert str(order_exmpl.product) == "Яблоко, 30.5 руб. Остаток: 53 шт."
