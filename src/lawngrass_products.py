from src.products import Product


class LawnGrass(Product):
    """Класс описывает шаблон товара - газонную траву"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализация газонной травы"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Product) -> int:
        if type(other) is LawnGrass:
            return self.quantity + other.quantity
        else:
            raise TypeError(f"Вы пытаетесь сложить объекты {self.__class__.__name__} " f"и {other.__class__.__name__}")
