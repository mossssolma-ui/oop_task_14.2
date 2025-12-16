import builtins

import pytest
from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch

from src.products import Product


def test_product_init(product: Product) -> None:
    """Тест инициализации экземпляра Product"""
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_price_setter_posit(product: Product) -> None:
    """Тест установки корректной (положительной) цены."""
    original_price = product.price
    new_price = original_price + 10000.0
    product.price = new_price
    assert product.price == new_price


def test_price_setter_negat(product: Product, capsys: CaptureFixture) -> None:
    """Тест установки отрицательной цены (должно игнорироваться)."""
    original_price = product.price
    product.price = -500.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == original_price


def test_price_setter(product: Product, monkeypatch: MonkeyPatch) -> None:
    """Тест понижения цены с подтверждением 'y'."""
    original_price = product.price
    new_price = original_price - 10000.0

    monkeypatch.setattr(builtins, "input", lambda _: "y")

    product.price = new_price
    assert product.price == new_price


def test_price_setter_not_conf(product: Product, monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
    """Тест понижения цены без подтверждения (ввод 'n' или любой другой)."""
    original_price = product.price
    new_price = original_price - 10000.0

    monkeypatch.setattr(builtins, "input", lambda _: "n")

    product.price = new_price
    captured = capsys.readouterr()
    assert "Отмена" in captured.out
    assert product.price == original_price


def test_new_product_create() -> None:
    """Тест создания нового продукта без дубликатов."""
    data = {"name": "Ноутбук", "description": "Игровой", "price": 150000.0, "quantity": 3}
    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Ноутбук"
    assert product.price == 150000.0
    assert product.quantity == 3


def test_new_product_updates_existing_duplicate(monkeypatch: MonkeyPatch) -> None:
    """Тест обновления существующего продукта при дубликате."""
    monkeypatch.setattr(builtins, "input", lambda _: "y")

    existing = Product("Смартфон", "Топовый", 100000.0, 5)
    products_list = [existing]

    new_data = {"name": "Смартфон", "description": "Новое описание", "price": 120000.0, "quantity": 2}
    result = Product.new_product(new_data, products_list)

    assert result is existing
    assert result.quantity == 7
    assert result.price == 120000.0


def test_product_add(test_product1: Product, test_product2: Product) -> None:
    res = test_product1 + test_product2
    expected = test_product1.quantity * test_product1.price + test_product2.quantity * test_product2.price
    assert res == expected
    with pytest.raises(TypeError):
        res = test_product1 + 100  # type:ignore
