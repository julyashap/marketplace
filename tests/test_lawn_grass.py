import pytest
from src.lawn_grass import LawnGrass
from src.product import Product


@pytest.fixture
def lawn_grass_exmpl():
    Product.count_products = 0

    return LawnGrass('Трава зеленая', 'Зеленая трава для футбола',
                      150000.0, 2, 'Россия', 120.5, 'Зеленый')


@pytest.fixture
def lawn_grass_dict():
    return {
        "name": "Трава зеленая",
        "description": "Зеленая трава для футбола",
        "price": 150000.0,
        "quantity": 2,
        "country": 150,
        "growing_period": 120.5,
        "color": "Зеленый"
    }


def test_init(lawn_grass_exmpl):
    """Тест конструктора класса Product"""

    assert lawn_grass_exmpl.name == 'Трава зеленая'
    assert lawn_grass_exmpl.description == 'Зеленая трава для футбола'
    assert lawn_grass_exmpl.get_cost == 150000.0
    assert lawn_grass_exmpl.count_in_stock == 2
    assert lawn_grass_exmpl.country == 'Россия'
    assert lawn_grass_exmpl.growing_period == 120.5
    assert lawn_grass_exmpl.color == 'Зеленый'

    assert Product.count_products == 1


def test_create_product(lawn_grass_dict):
    assert type(LawnGrass.create_product(lawn_grass_dict)) == LawnGrass
