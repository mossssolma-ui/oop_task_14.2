from typing import Any


class PrintMixin:
    name: Any
    description: Any
    price: Any
    quantity: Any

    def __init__(self) -> None:
        """Выводит сообщение для экземпляра"""
        print(repr(self))

    def __repr__(self) -> str:
        """
        Возвращает строку в таком шаблоне
        Product('Продукт1', 'Описание продукта', 1200, 10)
        """
        return f"{self.__class__.__name__}" f"({self.name}, {self.description}, {self.price}, {self.quantity})"
