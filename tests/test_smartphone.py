import pytest
from src.smartphone import Smartphone
from src.product import Product


@pytest.fixture
def smartphone_exmpl():
    Product.count_products = 0

    return Smartphone('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера',
                      180000.0, 5, 125, 'Samsung', 256, 'Grey')


@pytest.fixture
def smartphone_dict():
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "capacity": 125,
        "model": "Samsung",
        "memory": 256,
        "color": "Red"
      }


def test_init(smartphone_exmpl):
    """Тест конструктора класса Product"""

    assert smartphone_exmpl.name == 'Samsung Galaxy C23 Ultra'
    assert smartphone_exmpl.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_exmpl.get_cost == 180000.0
    assert smartphone_exmpl.count_in_stock == 5
    assert smartphone_exmpl.capacity == 125
    assert smartphone_exmpl.model == 'Samsung'
    assert smartphone_exmpl.memory == 256
    assert smartphone_exmpl.color == 'Grey'

    assert Product.count_products == 1


def test_create_product(smartphone_dict):
    assert type(Smartphone.create_product(smartphone_dict)) == Smartphone


def test_repr(smartphone_exmpl):
    assert repr(smartphone_exmpl) == "Smartphone('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', " \
                                     "180000.0, 5, 125, 'Samsung', 256, 'Grey')"
