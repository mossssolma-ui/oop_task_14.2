import pytest

from src.lawngrass_products import LawnGrass
from src.smartphone_products import Smartphone


def test_smartphone_products_init(products_smartphone1: Smartphone) -> None:
    """Тест на инициализацию конструктора"""
    assert products_smartphone1.name == "Iphone 15"
    assert products_smartphone1.description == "512GB, Gray space"
    assert products_smartphone1.price == 210000.0
    assert products_smartphone1.quantity == 8
    assert products_smartphone1.efficiency == 98.2
    assert products_smartphone1.model == "15"
    assert products_smartphone1.memory == 512
    assert products_smartphone1.color == "Gray space"


def test_smartphone_products_add_item(products_smartphone1: Smartphone, products_smartphone2: Smartphone) -> None:
    """Тест на проверку суммы"""
    assert products_smartphone1 + products_smartphone2 == 22


def test_smartphone_products_add_error(products_lawngrass1: LawnGrass, products_smartphone1: Smartphone) -> None:
    """Тест на ошибку при сумме разных объектов"""
    with pytest.raises(TypeError):
        products_lawngrass1 + products_smartphone1
