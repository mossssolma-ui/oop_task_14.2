from src.products import Product


class Category:
    """Класс описывает карточку категории"""

    name: str
    description: str
    products: list[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product] | None = None) -> None:
        """Инициализация категории"""
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.products)
