from src.categories import Category
from src.products import Product


class CategoryIterator:
    """
    Класс, в котором реализован протокол итерации
    Принимает на вход объект класса категории и производить итерацию по товарам,
    которые хранятся в данной категории.
    """

    def __init__(self, category_obj: Category) -> None:
        """Инициализация конструктора"""
        self.category = category_obj

    def __iter__(self) -> CategoryIterator:
        """Возвращает сам объект итерации"""
        self.index = 0
        return self

    def __next__(self) -> Product:
        """Возвращает значение итерации"""
        if self.index < len(self.category.product_obj):
            prod = self.category.product_obj[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3],
#     )
#     iterator = CategoryIterator(category1)
#     for cat in iterator:
#         print(cat)
