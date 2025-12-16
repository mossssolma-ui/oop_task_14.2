from src.products import Product


class Category:
    """
    Класс описывает категорию товаров и управляет списком продуктов в ней
    """

    name: str
    description: str
    __products: list[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product] | None = None) -> None:
        """Инициализация категории"""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """
        Считает общее количество продуктов
        и позволяет выводить строковое отображение в таком формате:
        Название категории, количество продуктов: 200 шт.
        """
        total_count = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_count} шт."

    def add_product(self, product: Product) -> None:
        """Добавление продукта в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Выводит список товаров в виде строк в формате:
        Название продукта, 80 руб. Остаток: 15 шт.
        """
        prod_str = ""
        for product in self.__products:
            prod_str += f"{str(product)}\n"
        return prod_str

    @property
    def products_count(self) -> int:
        """Возвращает количество товаров в категории"""
        return len(self.__products)

    @property
    def product_obj(self) -> list[Product]:
        """Возвращает список объектов Product"""
        return self.__products
