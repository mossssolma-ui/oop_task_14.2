from src.products import Product


class Smartphone(Product):
    """Класс описывает шаблон товара - смартфон"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализация смартфона"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Product) -> int:
        if type(other) is Smartphone:
            return self.quantity + other.quantity
        else:
            raise TypeError(f"Вы пытаетесь сложить объекты {self.__class__.__name__} " f"и {other.__class__.__name__}")
