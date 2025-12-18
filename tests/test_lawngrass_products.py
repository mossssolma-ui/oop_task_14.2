import pytest

from src.lawngrass_products import LawnGrass
from src.smartphone_products import Smartphone


def test_lawngrass_products_init(products_lawngrass1: LawnGrass) -> None:
    """Тест на инициализацию конструктора"""
    assert products_lawngrass1.name == "Газонная трава"
    assert products_lawngrass1.description == "Элитная трава для газона"
    assert products_lawngrass1.price == 500.0
    assert products_lawngrass1.quantity == 20
    assert products_lawngrass1.country == "Россия"
    assert products_lawngrass1.germination_period == "7 дней"
    assert products_lawngrass1.color == "Зеленый"


def test_lawngrass_products_add_item(products_lawngrass1: LawnGrass, products_lawngrass2: LawnGrass) -> None:
    """Тест на проверку суммы"""
    assert products_lawngrass1 + products_lawngrass2 == 35


def test_lawngrass_products_add_error(products_lawngrass1: LawnGrass, products_smartphone1: Smartphone) -> None:
    """Тест на ошибку при сумме разных объектов"""
    with pytest.raises(TypeError):
        products_lawngrass1 + products_smartphone1
