from abc import ABC

from src.base_products import BaseProduct


def test_base_product_is_abstract() -> None:
    """Тест, что BaseProduct — абстрактный класс."""
    assert issubclass(BaseProduct, ABC)
