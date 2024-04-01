import pytest
from src.mixin_repr import MixinRepr
from src.smartphone import Smartphone
from src.category import Category
from src.product import Product


def test_init_smartphone(capsys):
    smartphone = Smartphone('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера',
                      180000.0, 5, 125, 'Samsung', 256, 'Grey')

    captured = capsys.readouterr()
    assert "Smartphone('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', " \
           "180000.0, 5, 125, 'Samsung', 256, 'Grey')" in captured.out


def test_init_category(capsys):
    category = Category('Еда', 'Для утоления голода', [Product('Яблоко', 'Полезный фрукт', 30.5, 53),
                                                   Product('Пельмени', 'Вкусный и сытный обед', 214.99, 152)])

    captured = capsys.readouterr()
    assert "Category('Еда', 'Для утоления голода', [Product('Яблоко', 'Полезный фрукт', 30.5, 53), " \
           "Product('Пельмени', 'Вкусный и сытный обед', 214.99, 152)])" in captured.out


def test_repr_product():
    product = Product('Яблоко', 'Полезный фрукт', 30.5, 53)

    assert repr(product) == "Product('Яблоко', 'Полезный фрукт', 30.5, 53)"
