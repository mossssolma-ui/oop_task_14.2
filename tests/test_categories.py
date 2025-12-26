from _pytest.capture import CaptureFixture

from src.categories import Category
from src.products import Product


def test_category_init(first_category: Category, second_category: Category) -> None:
    """Тест инициализации отдельной Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство получения дополнительных функций для удобства жизни"
    assert first_category.products_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5

    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_category_empty_initialization() -> None:
    """Тест инициализации категории без товаров."""
    category = Category("Пустая категория", "Описание пустой категории")
    assert category.name == "Пустая категория"
    assert category.description == "Описание пустой категории"
    assert category.products_count == 0
    assert category.products == ""


def test_add_product_method() -> None:
    """Тест метода добавления продукта в категорию."""
    category = Category("Новая категория", "Описание")
    product = Product("Новый товар", "Описание товара", 1000.0, 10)

    assert category.products_count == 0
    assert category.products == ""

    category.add_product(product)

    assert category.products_count == 1
    assert "Новый товар, 1000 руб. Остаток: 10 шт.\n" in category.products
    assert category.product_obj[0] == product


def test_products_format() -> None:
    """Тест корректного формата строки свойства products."""
    product1 = Product("Телефон", "Смартфон", 50000.0, 7)
    product2 = Product("Наушники", "Беспроводные", 5000.0, 15)
    category = Category("Электроника", "Гаджеты", [product1, product2])

    expected_out = "Телефон, 50000 руб. Остаток: 7 шт.\n" "Наушники, 5000 руб. Остаток: 15 шт.\n"
    assert category.products == expected_out


def test_product_returns_list_products() -> None:
    """Тест свойства product_obj: возвращает список объектов Product."""
    product1 = Product("A", "Desc A", 10.0, 1)
    product2 = Product("B", "Desc B", 20.0, 2)
    category = Category("Тест", "Тестовая категория", [product1, product2])

    products_list = category.product_obj
    assert isinstance(products_list, list)
    assert len(products_list) == 2
    assert products_list[0] == product1
    assert products_list[1] == product2
    assert products_list[0].name == "A"
    assert products_list[1].quantity == 2


def test_category_add_product() -> None:
    """Тест корректности счётчиков при добавлении товара через add_product."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Товар1", "Описание1", 100.0, 5)
    cat = Category("Категория", "Описание", [product1])
    assert Category.category_count == 1
    assert Category.product_count == 1

    product2 = Product("Товар2", "Описание2", 200.0, 3)
    cat.add_product(product2)
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_categories_str(first_category: Product) -> None:
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."


def test_middle_price(first_category: Category, empty_category_products: Category) -> None:
    assert first_category.middle_price() == 195000.0
    assert empty_category_products.middle_price() == 0.0


def test_middle_price_with_products():

    product1 = Product("Товар 1", "Описание 1", 100.0, 10)
    product2 = Product("Товар 2", "Описание 2", 200.0, 5)
    product3 = Product("Товар 3", "Описание 3", 300.0, 15)

    category = Category("Категория 1", "Описание категории", [product1, product2, product3])

    result = category.middle_price()
    expected = (100 + 200 + 300) / 3
    assert result == expected
