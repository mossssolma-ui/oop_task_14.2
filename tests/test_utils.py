import json
from unittest.mock import Mock

import pytest

from src.categories import Category
from src.products import Product
from src.utils import create_objects_from_json, read_json


def test_read_json(tmp_path: Mock, sample_json_data: dict) -> None:
    """Тест успешного чтения json"""
    json_file = tmp_path / "test_data.json"
    json_file.write_text(json.dumps(sample_json_data, ensure_ascii=False), encoding="utf-8")

    res = read_json(str(json_file))
    assert res == sample_json_data


def test_read_json_failed(tmp_path: Mock) -> None:
    """Тест неуспешного чтения json (отсутствие файла)"""
    with pytest.raises(FileNotFoundError):
        read_json("test_data.json")


def test_create_objects_from_json_success(create_sample_json_data: dict) -> None:
    """Тест успешного создания объекта"""
    categories = create_objects_from_json(create_sample_json_data)

    assert len(categories) == 2
    assert isinstance(categories[0], Category)
    assert isinstance(categories[1], Category)

    cat1 = categories[0]
    assert cat1.name == "Смартфоны"
    assert (
        cat1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert cat1.products_count == 2
    assert isinstance(cat1.product_obj[0], Product)
    assert cat1.product_obj[0].name == "Samsung Galaxy C23 Ultra"
    assert cat1.product_obj[1].name == "Iphone 15"

    cat2 = categories[1]
    assert cat2.name == "Телевизоры"
    assert cat2.products_count == 1
    assert cat2.product_obj[0].quantity == 7
