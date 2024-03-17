import pytest
from src.product import Product
from unittest.mock import patch

@pytest.fixture
def product_exmpl():
    """Тестовый экземпляр класса Product"""

    return Product("Яблоко", "Полезный фрукт", 30.5, 53)


@pytest.fixture
def product_dict():
    """Тестовый словарь с данными о продукте"""

    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }


def test_init(product_exmpl):
    """Тест конструктора класса Product"""

    assert product_exmpl.name == "Яблоко"
    assert product_exmpl.description == "Полезный фрукт"
    assert product_exmpl.count_in_stock == 53

    assert Product.count_products == 8


def test_create_product(product_exmpl, product_dict):
    """Тест метода create_product()"""

    assert type(Product.create_product(product_dict)) == Product


def test_get_cost(product_exmpl):
    """Тест метода get_cost()"""

    assert product_exmpl.get_cost == 30.5


def test_set_cost(product_exmpl, capsys):
    """Тест метода set_cost() для случая смены цены и задавемая когда цена <= 0"""

    product_exmpl.set_cost = 200.0
    assert product_exmpl.get_cost == 200.0

    product_exmpl.set_cost = -500
    captured = capsys.readouterr()
    assert "Некорректная цена!" in captured.out
    assert product_exmpl.get_cost == 200.0


'''def test_set_cost_no_change(product_exmpl, mocker):
    """Тест метода set_cost() для случая отказа снизить цену"""

    mocker.patch('builtins.input', return_value='n')

    product_exmpl.set_cost = 50.0
    assert product_exmpl._Product__cost == 200.0


def test_set_cost_lower_price(product_exmpl, mocker):
    """Тест метода set_cost() для случая согласия снизить цену"""

    mocker.patch('builtins.input', return_value='y')

    product_exmpl.set_cost = 50.0
    assert product_exmpl._Product__cost == 50.0'''
