import pytest

from src.categ_iterator import CategoryIterator


def test_categ_iterator_init(category_iterator: CategoryIterator) -> None:
    """Инициализация итератора"""
    assert isinstance(category_iterator, CategoryIterator)


def test_iter_cat(category_iterator: CategoryIterator) -> None:
    """Тест, что __iter__ возвращает сам итератор"""
    res = iter(category_iterator)
    assert str(next(res)) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."


def test_next_raises(category_iterator: CategoryIterator) -> None:
    """Тест вызова StopIteration"""
    iterator = iter(category_iterator)
    for _ in range(3):
        next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)
