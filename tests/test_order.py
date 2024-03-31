import pytest
from src.order import Order
from src.product import Product

@pytest.fixture
def order_exmpl():
    Product.count_products = 0

    return Order(Product('Груша', 'Полезный фрукт', 60.0, 24), 15)

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
