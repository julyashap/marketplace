import pytest
from src.zero_count_error import ZeroCountError


@pytest.fixture
def zero_count_error_exmpl():
    return ZeroCountError()


@pytest.fixture
def zero_count_error_exmpl2():
    return ZeroCountError("Ошибка")


def test_init(zero_count_error_exmpl, zero_count_error_exmpl2):
    assert zero_count_error_exmpl.message == "Количество продукта не может быть нулевым!"
    assert zero_count_error_exmpl2.message == "Ошибка"


def test_str(zero_count_error_exmpl):
    assert str(zero_count_error_exmpl) == "Количество продукта не может быть нулевым!"
